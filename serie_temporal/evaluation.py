"""Métricas y gráficas para comparar valores reales vs. predicciones."""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend sin ventana: permite guardar PNG en cualquier entorno
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# --- Métricas -------------------------------------------------------------------
def _alinear(y_real: pd.Series, y_pred: pd.Series) -> tuple[np.ndarray, np.ndarray]:
    datos = pd.concat([y_real.rename("real"), y_pred.rename("pred")], axis=1).dropna()
    if datos.empty:
        raise ValueError("No hay pares real/predicción para evaluar.")
    return datos["real"].to_numpy(float), datos["pred"].to_numpy(float)


def mae(y_real: pd.Series, y_pred: pd.Series) -> float:
    """Error absoluto medio: en promedio, cuántos pesos se equivoca el modelo."""
    r, p = _alinear(y_real, y_pred)
    return float(np.mean(np.abs(r - p)))


def rmse(y_real: pd.Series, y_pred: pd.Series) -> float:
    """Raíz del error cuadrático medio: penaliza más los errores grandes."""
    r, p = _alinear(y_real, y_pred)
    return float(np.sqrt(np.mean((r - p) ** 2)))


def mape(y_real: pd.Series, y_pred: pd.Series) -> float:
    """Error porcentual absoluto medio (%), útil para interpretar en términos relativos."""
    r, p = _alinear(y_real, y_pred)
    return float(np.mean(np.abs((r - p) / r)) * 100)


def tabla_metricas(y_real: pd.Series, predicciones: dict[str, pd.Series]) -> pd.DataFrame:
    """Tabla comparativa de todos los modelos, ordenada por RMSE."""
    filas = [
        {"modelo": nombre, "MAE": mae(y_real, pred), "RMSE": rmse(y_real, pred), "MAPE_%": mape(y_real, pred)}
        for nombre, pred in predicciones.items()
    ]
    tabla = pd.DataFrame(filas).sort_values("RMSE").reset_index(drop=True)
    return tabla.round({"MAE": 2, "RMSE": 2, "MAPE_%": 3})


# --- Gráficas -------------------------------------------------------------------
def _formato_eje(ax: plt.Axes, titulo: str) -> None:
    ax.set_title(titulo)
    ax.set_xlabel("Fecha")
    ax.set_ylabel("TRM (COP por USD)")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.legend()


def graficar_serie(serie: pd.Series, train: pd.Series, test: pd.Series, ruta: Path, ventana: int) -> None:
    """Serie completa con la división entrenamiento/prueba y la media móvil."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(train.index, train, color="tab:blue", lw=1, label="Entrenamiento")
    ax.plot(test.index, test, color="tab:orange", lw=1, label="Prueba")
    ax.plot(serie.index, serie.rolling(ventana).mean(), color="black", lw=0.8, alpha=0.6,
            label=f"Media móvil {ventana}")
    ax.axvline(test.index[0], color="gray", ls=":", lw=1)
    _formato_eje(ax, "TRM diaria USD/COP - división temporal entrenamiento/prueba")
    fig.tight_layout()
    fig.savefig(ruta, dpi=150)
    plt.close(fig)


def graficar_real_vs_pred(test: pd.Series, predicciones: dict[str, pd.Series], ruta: Path) -> None:
    """Valores reales del tramo de prueba vs. la predicción de cada modelo."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(test.index, test, color="black", lw=1.6, label="Real")
    for nombre, pred in predicciones.items():
        ax.plot(pred.index, pred, lw=1, alpha=0.85, label=nombre)
    _formato_eje(ax, "Tramo de prueba: real vs. predicción a un paso")
    fig.tight_layout()
    fig.savefig(ruta, dpi=150)
    plt.close(fig)


def graficar_errores(test: pd.Series, predicciones: dict[str, pd.Series], ruta: Path) -> None:
    """Error (real - predicción) de cada modelo a lo largo del tramo de prueba."""
    fig, ax = plt.subplots(figsize=(12, 4))
    for nombre, pred in predicciones.items():
        ax.plot(pred.index, test - pred, lw=0.9, label=nombre)
    ax.axhline(0, color="black", lw=0.8)
    _formato_eje(ax, "Error de predicción (real - predicho)")
    ax.set_ylabel("COP")
    fig.tight_layout()
    fig.savefig(ruta, dpi=150)
    plt.close(fig)


def graficar_pronostico(serie: pd.Series, futuro: pd.Series, ruta: Path, historia: int = 120) -> None:
    """Últimos `historia` datos reales + pronóstico recursivo hacia adelante."""
    reciente = serie.iloc[-historia:]
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(reciente.index, reciente, color="tab:blue", lw=1.2, label="Histórico reciente")
    unido = pd.concat([reciente.iloc[-1:], futuro])
    ax.plot(unido.index, unido, color="tab:red", lw=1.4, ls="--", marker="o", ms=3,
            label=f"Pronóstico próximas {len(futuro)} TRM")
    _formato_eje(ax, "Pronóstico de la TRM (regresión autorregresiva)")
    fig.tight_layout()
    fig.savefig(ruta, dpi=150)
    plt.close(fig)
