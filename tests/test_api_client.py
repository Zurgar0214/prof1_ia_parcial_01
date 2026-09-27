"""Pruebas del cliente HTTP sin red: se simula la respuesta de la API."""
import pytest

import api_client
from test_preprocessing import REALES


class RespuestaFalsa:
    def __init__(self, status=200, datos=None, texto=""):
        self.status_code, self._datos, self.text = status, datos, texto

    def json(self):
        if isinstance(self._datos, Exception):
            raise self._datos
        return self._datos


class SesionFalsa:
    """Devuelve las páginas indicadas en orden y registra los parámetros enviados."""

    def __init__(self, respuestas):
        self.respuestas, self.llamadas = list(respuestas), []

    def get(self, url, params=None, headers=None, timeout=None):
        self.llamadas.append({"url": url, "params": params, "headers": headers})
        return self.respuestas.pop(0)


def test_paginacion_y_metadatos():
    sesion = SesionFalsa([RespuestaFalsa(datos=REALES[:2]), RespuestaFalsa(datos=REALES[2:3])])
    registros, meta = api_client.obtener_trm("2026-09-01", "2026-09-22", app_token=None, page_size=2, session=sesion)
    assert len(registros) == 3 and meta["paginas"] == 2
    assert sesion.llamadas[1]["params"]["$offset"] == 2
    assert "X-App-Token" not in sesion.llamadas[0]["headers"]


def test_token_va_en_cabecera_y_no_en_metadatos():
    sesion = SesionFalsa([RespuestaFalsa(datos=REALES)])
    _, meta = api_client.obtener_trm("2026-09-01", "2026-09-22", app_token="secreto", session=sesion)
    assert sesion.llamadas[0]["headers"]["X-App-Token"] == "secreto"
    assert "secreto" not in str(meta)


@pytest.mark.parametrize("respuesta", [
    RespuestaFalsa(status=500, texto="error"),
    RespuestaFalsa(datos=ValueError("no json")),
    RespuestaFalsa(datos={"error": True}),
    RespuestaFalsa(datos=[{"valor": "1"}]),
    RespuestaFalsa(datos=[]),
])
def test_respuestas_invalidas(respuesta):
    with pytest.raises(api_client.APIError):
        api_client.obtener_trm("2026-09-01", "2026-09-22", app_token=None, session=SesionFalsa([respuesta]))
