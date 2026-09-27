"""Pruebas de validación y preparación de datos.

El fixture usa 5 registros REALES devueltos por la API el 2026-09-22,
en desorden y con un duplicado, un valor no numérico y un faltante añadidos
a propósito para comprobar que la validación los detecta.
"""
import pandas as pd
import pytest

import preprocessing

REALES = [
    {"valor": "3192.53", "unidad": "COP", "vigenciadesde": "2026-09-22T00:00:00.000", "vigenciahasta": "2026-09-22T00:00:00.000"},
    {"valor": "3192.92", "unidad": "COP", "vigenciadesde": "2026-09-19T00:00:00.000", "vigenciahasta": "2026-09-21T00:00:00.000"},
    {"valor": "3151.73", "unidad": "COP", "vigenciadesde": "2026-09-18T00:00:00.000", "vigenciahasta": "2026-09-18T00:00:00.000"},
    {"valor": "3128.46", "unidad": "COP", "vigenciadesde": "2026-09-17T00:00:00.000", "vigenciahasta": "2026-09-17T00:00:00.000"},
    {"valor": "3100.45", "unidad": "COP", "vigenciadesde": "2026-09-16T00:00:00.000", "vigenciahasta": "2026-09-16T00:00:00.000"},
]


def test_tipos_y_orden_con_datos_reales():
    df, rep = preprocessing.a_dataframe(REALES)
    assert df["valor"].dtype == "float64"
    assert pd.api.types.is_datetime64_any_dtype(df["vigenciadesde"])
    assert df["vigenciadesde"].is_monotonic_increasing
    assert rep.estaba_ordenada is False  # la API se consultó en orden DESC
    assert rep.huecos_vigencia == 0 and rep.traslapes_vigencia == 0  # sábado->lunes es continuo
    assert rep.unidades == ["COP"]
    assert df["valor"].iloc[0] == pytest.approx(3100.45)


def test_detecta_faltantes_duplicados_y_no_numericos():
    sucios = REALES + [
        dict(REALES[0]),                                                 # duplicado
        {**REALES[0], "valor": "N/D", "vigenciadesde": "2026-09-23T00:00:00.000"},  # no numérico
        {**REALES[0], "valor": None, "vigenciadesde": "2026-09-24T00:00:00.000"},   # faltante
    ]
    df, rep = preprocessing.a_dataframe(sucios)
    assert rep.valores_no_numericos == 1
    assert rep.faltantes_eliminados == 2
    assert rep.duplicados_eliminados == 1
    assert rep.registros_finales == 5 == len(df)


def test_detecta_hueco_de_vigencia():
    con_hueco = [r for r in REALES if not r["vigenciadesde"].startswith("2026-09-17")]
    _, rep = preprocessing.a_dataframe(con_hueco)
    assert rep.huecos_vigencia == 1


def test_split_respeta_orden_temporal():
    serie = pd.Series(range(100), index=pd.bdate_range("2024-01-01", periods=100), dtype=float)
    train, test = preprocessing.dividir_train_test(serie, 0.2)
    assert len(train) == 80 and len(test) == 20
    assert train.index.max() < test.index.min()


def test_split_invalido():
    serie = pd.Series([1.0, 2.0], index=pd.bdate_range("2024-01-01", periods=2))
    with pytest.raises(ValueError):
        preprocessing.dividir_train_test(serie, 1.5)
