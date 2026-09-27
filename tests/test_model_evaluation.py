"""Pruebas de baselines, regresión AR (sin fuga de información) y métricas."""
import numpy as np
import pandas as pd
import pytest

import evaluation
import model


@pytest.fixture
def serie():
    rng = np.random.default_rng(42)
    valores = 4000 + np.cumsum(rng.normal(0, 10, 300))  # caminata aleatoria sintética
    return pd.Series(valores, index=pd.bdate_range("2024-01-01", periods=300), name="trm")


def test_persistencia_es_valor_anterior(serie):
    idx = serie.index[-5:]
    pred = model.pronostico_persistencia(serie, idx)
    assert np.allclose(pred.to_numpy(), serie.iloc[-6:-1].to_numpy())


def test_media_movil_no_incluye_valor_actual(serie):
    idx = serie.index[-1:]
    pred = model.pronostico_media_movil(serie, idx, 3)
    assert pred.iloc[0] == pytest.approx(serie.iloc[-4:-1].mean())


def test_regresion_no_usa_informacion_futura(serie):
    train, test = serie.iloc[:240], serie.iloc[240:]
    reg = model.RegresionAutorregresiva(3).entrenar(train)
    pred_original = reg.pronosticar_un_paso(serie, test.index)
    # Si alteramos el valor de un día t, la predicción de ese mismo día NO debe cambiar
    alterada = serie.copy()
    alterada.iloc[250] += 1_000
    pred_alterada = reg.pronosticar_un_paso(alterada, test.index)
    assert pred_alterada.iloc[10] == pytest.approx(pred_original.iloc[10])
    assert pred_alterada.iloc[11] != pytest.approx(pred_original.iloc[11])  # sí afecta al día siguiente


def test_regresion_aprende_proceso_lineal():
    idx = pd.bdate_range("2024-01-01", periods=200)
    y = pd.Series(100 + 2.0 * np.arange(200), index=idx)  # tendencia perfecta
    reg = model.RegresionAutorregresiva(2).entrenar(y.iloc[:150])
    pred = reg.pronosticar_un_paso(y, y.index[150:])
    assert evaluation.mae(y.iloc[150:], pred) < 1e-6


def test_pronostico_futuro_en_dias_habiles(serie):
    reg = model.RegresionAutorregresiva(5).entrenar(serie)
    fut = reg.pronosticar_futuro(serie, 10)
    assert len(fut) == 10
    assert fut.index.min() > serie.index.max()
    assert all(d.weekday() < 5 for d in fut.index)


def test_pronostico_futuro_con_fechas_de_vigencia(serie):
    reg = model.RegresionAutorregresiva(5).entrenar(serie)
    fechas = pd.bdate_range("2026-09-29", periods=5, freq="C", weekmask="Tue Wed Thu Fri Sat")
    fut = reg.pronosticar_futuro(serie, 5, fechas)
    assert list(fut.index) == list(fechas)
    assert all(d.weekday() in (1, 2, 3, 4, 5) for d in fut.index)  # martes a sábado
    with pytest.raises(ValueError):
        reg.pronosticar_futuro(serie, 3, fechas)


def test_modelo_sin_entrenar():
    with pytest.raises(RuntimeError):
        model.RegresionAutorregresiva(2).coeficientes()


def test_metricas_valores_conocidos():
    real = pd.Series([10.0, 20.0, 30.0])
    pred = pd.Series([12.0, 18.0, 33.0])
    assert evaluation.mae(real, pred) == pytest.approx((2 + 2 + 3) / 3)
    assert evaluation.rmse(real, pred) == pytest.approx(np.sqrt((4 + 4 + 9) / 3))


def test_tabla_metricas_ordena_por_rmse():
    real = pd.Series([1.0, 2.0, 3.0])
    tabla = evaluation.tabla_metricas(real, {"malo": real + 5, "bueno": real + 1})
    assert list(tabla["modelo"]) == ["bueno", "malo"]
