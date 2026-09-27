"""Modelos de pronóstico: dos baselines y un método predictivo básico.

Todos los modelos pronostican UN paso adelante (el siguiente día hábil) usando
solo información disponible hasta el día anterior (validación walk-forward):
para predecir y[t] se usan y[t-1], y[t-2], ... nunca y[t] ni valores posteriores.

- Persistencia (naive):      ŷ[t] = y[t-1]
- Media móvil (k):           ŷ[t] = promedio(y[t-k] ... y[t-1])
- Regresión autorregresiva:  ŷ[t] = b0 + b1·y[t-1] + ... + bp·y[t-p]
  (LinearRegression de scikit-learn entrenada SOLO con el tramo de entrenamiento)
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


# --- Baselines --------------------------------------------------------------------
def pronostico_persistencia(serie: pd.Series, indices_prueba: pd.Index) -> pd.Series:
    """ŷ[t] = y[t-1]. El valor de ayer es el pronóstico de hoy."""
    return serie.shift(1).loc[indices_prueba].rename("persistencia")


def pronostico_media_movil(serie: pd.Series, indices_prueba: pd.Index, ventana: int) -> pd.Series:
    """ŷ[t] = media de las `ventana` observaciones anteriores a t."""
    if ventana < 1:
        raise ValueError("La ventana debe ser >= 1.")
    # shift(1) garantiza que la ventana termina en t-1 (no incluye el valor a predecir)
    return serie.rolling(ventana).mean().shift(1).loc[indices_prueba].rename(f"media_movil_{ventana}")


# --- Modelo predictivo ---------------------------------------------------------------
def crear_rezagos(serie: pd.Series, n_rezagos: int) -> pd.DataFrame:
    """Matriz de características: columnas lag_1 ... lag_p (valores pasados)."""
    if n_rezagos < 1:
        raise ValueError("n_rezagos debe ser >= 1.")
    return pd.concat({f"lag_{k}": serie.shift(k) for k in range(1, n_rezagos + 1)}, axis=1)


class RegresionAutorregresiva:
    """Regresión lineal sobre rezagos, AR(p), implementada con scikit-learn."""

    def __init__(self, n_rezagos: int = 5) -> None:
        self.n_rezagos = n_rezagos
        self.modelo = LinearRegression()
        self._entrenado = False

    def entrenar(self, serie_train: pd.Series) -> "RegresionAutorregresiva":
        X = crear_rezagos(serie_train, self.n_rezagos)
        datos = pd.concat([X, serie_train.rename("y")], axis=1).dropna()
        if len(datos) < self.n_rezagos + 2:
            raise ValueError("No hay suficientes datos de entrenamiento para los rezagos pedidos.")
        self.modelo.fit(datos[X.columns], datos["y"])
        self._entrenado = True
        return self

    def coeficientes(self) -> dict[str, float]:
        self._verificar()
        coefs = {f"lag_{k}": float(c) for k, c in enumerate(self.modelo.coef_, start=1)}
        coefs["intercepto"] = float(self.modelo.intercept_)
        return coefs

    def pronosticar_un_paso(self, serie_completa: pd.Series, indices_prueba: pd.Index) -> pd.Series:
        """Predicción walk-forward: para cada t de prueba usa los valores reales hasta t-1.

        Los rezagos se calculan sobre la serie completa, pero la fila de t solo
        contiene y[t-1..t-p]; y el modelo ya fue entrenado sin ver el tramo de prueba.
        """
        self._verificar()
        X = crear_rezagos(serie_completa, self.n_rezagos).loc[indices_prueba]
        if X.isna().any().any():
            raise ValueError("Faltan rezagos para algunas fechas de prueba.")
        pred = self.modelo.predict(X)
        return pd.Series(pred, index=indices_prueba, name=f"regresion_ar_{self.n_rezagos}")

    def pronosticar_futuro(
        self, serie: pd.Series, horizonte: int, fechas: pd.DatetimeIndex | None = None
    ) -> pd.Series:
        """Pronóstico recursivo de `horizonte` publicaciones después del último dato.

        Cada predicción se usa como rezago de la siguiente (el error se acumula,
        por eso la incertidumbre crece con el horizonte).
        `fechas`: fechas de inicio de vigencia de las próximas TRM (las calcula app.py
        a partir de la última `vigenciahasta`). Si no se dan, se usan días lunes-viernes
        posteriores al último dato. No descuenta festivos colombianos.
        """
        self._verificar()
        historia = list(serie.iloc[-self.n_rezagos:].to_numpy(dtype=float))
        if fechas is None:
            fechas = pd.bdate_range(serie.index[-1] + pd.Timedelta(days=1), periods=horizonte)
        if len(fechas) != horizonte:
            raise ValueError("Se necesita una fecha por cada paso del horizonte.")
        columnas = [f"lag_{k}" for k in range(1, self.n_rezagos + 1)]
        preds: list[float] = []
        for _ in range(horizonte):
            fila = pd.DataFrame([historia[::-1][: self.n_rezagos]], columns=columnas)
            y_hat = float(self.modelo.predict(fila)[0])
            preds.append(y_hat)
            historia.append(y_hat)
        return pd.Series(np.round(preds, 2), index=fechas, name="pronostico")

    def _verificar(self) -> None:
        if not self._entrenado:
            raise RuntimeError("El modelo debe entrenarse antes de pronosticar.")
