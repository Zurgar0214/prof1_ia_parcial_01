"""Preparación y validación de la serie temporal de la TRM.

Pasos:
1. JSON -> DataFrame con tipos correctos (float y datetime).
2. Validaciones: faltantes, tipos, duplicados, valores fuera de rango,
   unidad, orden temporal y continuidad de las vigencias.
3. Construcción de la serie: un valor por cada TRM publicada (día hábil),
   indexada por la fecha de inicio de su vigencia.

Decisión de diseño: la TRM de un viernes (o previa a festivo) rige varios días
calendario (p. ej. vigencia sábado->lunes). Si se expandiera a días calendario,
los fines de semana repetirían el mismo valor y los baselines parecerían
artificialmente buenos. Por eso se modela una observación por publicación.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pandas as pd


@dataclass
class ReporteCalidad:
    """Resultado de las validaciones; se imprime y se guarda como evidencia."""

    registros_recibidos: int = 0
    valores_no_numericos: int = 0
    fechas_invalidas: int = 0
    faltantes_eliminados: int = 0
    duplicados_eliminados: int = 0
    valores_no_positivos: int = 0
    unidades: list[str] = field(default_factory=list)
    estaba_ordenada: bool = True
    vigencias_invertidas: int = 0
    huecos_vigencia: int = 0
    traslapes_vigencia: int = 0
    registros_finales: int = 0
    fecha_min: str = ""
    fecha_max: str = ""

    def como_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


def a_dataframe(registros: list[dict[str, Any]]) -> tuple[pd.DataFrame, ReporteCalidad]:
    """Convierte la respuesta JSON en un DataFrame limpio y validado."""
    rep = ReporteCalidad(registros_recibidos=len(registros))
    df = pd.DataFrame.from_records(registros)

    # --- Tipos: la API entrega todo como texto --------------------------------
    valor = pd.to_numeric(df["valor"], errors="coerce")
    rep.valores_no_numericos = int(valor.isna().sum() - df["valor"].isna().sum())
    df["valor"] = valor.astype("float64")

    for col in ("vigenciadesde", "vigenciahasta"):
        fechas = pd.to_datetime(df[col], errors="coerce", format="ISO8601")
        rep.fechas_invalidas += int(fechas.isna().sum() - df[col].isna().sum())
        df[col] = fechas.dt.normalize()

    # --- Faltantes ---------------------------------------------------------------
    antes = len(df)
    df = df.dropna(subset=["valor", "vigenciadesde"])
    rep.faltantes_eliminados = antes - len(df)
    # Si falta vigenciahasta, se asume vigencia de un solo día.
    df["vigenciahasta"] = df["vigenciahasta"].fillna(df["vigenciadesde"])

    # --- Rango y unidad ------------------------------------------------------
    rep.valores_no_positivos = int((df["valor"] <= 0).sum())
    df = df[df["valor"] > 0]
    rep.unidades = sorted(df["unidad"].dropna().astype(str).unique().tolist()) if "unidad" in df else []

    # --- Orden temporal y duplicados ---------------------------------------------
    rep.estaba_ordenada = bool(df["vigenciadesde"].is_monotonic_increasing)
    df = df.sort_values("vigenciadesde", kind="stable")
    antes = len(df)
    df = df.drop_duplicates(subset="vigenciadesde", keep="last")
    rep.duplicados_eliminados = antes - len(df)

    # --- Coherencia de vigencias ---------------------------------------------------
    rep.vigencias_invertidas = int((df["vigenciahasta"] < df["vigenciadesde"]).sum())
    siguiente_inicio = df["vigenciadesde"].shift(-1)
    esperado = df["vigenciahasta"] + pd.Timedelta(days=1)
    comparables = siguiente_inicio.notna()
    rep.huecos_vigencia = int((siguiente_inicio[comparables] > esperado[comparables]).sum())
    rep.traslapes_vigencia = int((siguiente_inicio[comparables] < esperado[comparables]).sum())

    df = df.reset_index(drop=True)
    rep.registros_finales = len(df)
    if len(df):
        rep.fecha_min = df["vigenciadesde"].min().date().isoformat()
        rep.fecha_max = df["vigenciadesde"].max().date().isoformat()
    return df, rep


def construir_serie(df: pd.DataFrame) -> pd.Series:
    """Serie temporal: índice = fecha de inicio de vigencia, valor = TRM (COP/USD)."""
    serie = df.set_index("vigenciadesde")["valor"].rename("trm")
    serie.index.name = "fecha"
    if not serie.index.is_monotonic_increasing or serie.index.has_duplicates:
        raise ValueError("La serie debe tener fechas únicas y en orden ascendente.")
    return serie


def dividir_train_test(serie: pd.Series, test_size: float) -> tuple[pd.Series, pd.Series]:
    """Divide respetando el orden temporal: el pasado entrena, el futuro prueba.

    No se usa un split aleatorio: todas las fechas de prueba son posteriores a
    todas las de entrenamiento, así ninguna información futura entra al modelo.
    """
    if not 0 < test_size < 1:
        raise ValueError("test_size debe estar entre 0 y 1.")
    n_test = max(1, int(round(len(serie) * test_size)))
    if n_test >= len(serie):
        raise ValueError("La serie es demasiado corta para el test_size indicado.")
    return serie.iloc[:-n_test], serie.iloc[-n_test:]
