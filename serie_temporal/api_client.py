"""Cliente de la API pública de Datos Abiertos Colombia (Socrata) para la TRM.

Responsabilidad única: pedir los datos por HTTP, validar la respuesta y
devolver la lista de registros JSON tal como llega (sin transformarlos).

Ejemplo de registro devuelto por la API:
    {"valor": "3192.53", "unidad": "COP",
     "vigenciadesde": "2026-09-22T00:00:00.000",
     "vigenciahasta": "2026-09-22T00:00:00.000"}
"""
from __future__ import annotations

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

import config

CAMPOS_REQUERIDOS: tuple[str, ...] = ("valor", "unidad", "vigenciadesde", "vigenciahasta")


class APIError(RuntimeError):
    """Error controlado al consultar o validar la respuesta de la API."""


def _construir_parametros(fecha_inicio: str, fecha_fin: str, limit: int, offset: int) -> dict[str, Any]:
    """Arma la consulta SoQL: filtra por fecha, ordena y pagina."""
    return {
        "$select": ",".join(CAMPOS_REQUERIDOS),
        "$where": (
            f"vigenciadesde between '{fecha_inicio}T00:00:00' "
            f"and '{fecha_fin}T23:59:59'"
        ),
        "$order": "vigenciadesde ASC",
        "$limit": limit,
        "$offset": offset,
    }


def _validar_pagina(respuesta: requests.Response) -> list[dict[str, Any]]:
    """Valida código HTTP, formato JSON y campos esperados de una página."""
    if respuesta.status_code != 200:
        raise APIError(
            f"La API respondió HTTP {respuesta.status_code}: {respuesta.text[:200]}"
        )
    try:
        datos = respuesta.json()
    except ValueError as error:
        raise APIError("La respuesta de la API no es JSON válido.") from error

    if not isinstance(datos, list):
        raise APIError(f"Se esperaba una lista JSON y llegó {type(datos).__name__}.")

    for i, registro in enumerate(datos):
        faltantes = [c for c in CAMPOS_REQUERIDOS if c not in registro]
        if faltantes:
            raise APIError(f"El registro {i} no contiene los campos {faltantes}: {registro}")
    return datos


def obtener_trm(
    fecha_inicio: str = config.FECHA_INICIO,
    fecha_fin: str = config.FECHA_FIN,
    app_token: str | None = config.SOCRATA_APP_TOKEN,
    page_size: int = config.PAGE_SIZE,
    timeout: int = config.REQUEST_TIMEOUT,
    session: requests.Session | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Descarga todos los registros de TRM entre dos fechas (paginando).

    Returns:
        (registros, metadatos) donde metadatos documenta la consulta realizada
        (URL, fechas, páginas, tiempo, total) como evidencia de consumo de API.
    """
    http = session or requests.Session()
    headers = {"Accept": "application/json"}
    if app_token:
        headers["X-App-Token"] = app_token  # nunca se imprime ni se guarda

    registros: list[dict[str, Any]] = []
    offset, paginas = 0, 0
    inicio = time.perf_counter()

    while True:
        params = _construir_parametros(fecha_inicio, fecha_fin, page_size, offset)
        try:
            respuesta = http.get(config.API_URL, params=params, headers=headers, timeout=timeout)
        except requests.exceptions.RequestException as error:
            raise APIError(f"Error de red consultando {config.API_URL}: {error}") from error

        pagina = _validar_pagina(respuesta)
        paginas += 1
        registros.extend(pagina)
        if len(pagina) < page_size:
            break
        offset += page_size

    if not registros:
        raise APIError(f"La API no devolvió registros entre {fecha_inicio} y {fecha_fin}.")

    metadatos = {
        "fuente": "Datos Abiertos Colombia - TRM (Superintendencia Financiera)",
        "endpoint": config.API_URL,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "paginas": paginas,
        "registros": len(registros),
        "segundos": round(time.perf_counter() - inicio, 2),
        "consultado_en": datetime.now().isoformat(timespec="seconds"),
        "uso_app_token": bool(app_token),
    }
    return registros, metadatos


def guardar_json(registros: list[dict[str, Any]], metadatos: dict[str, Any], ruta: Path) -> None:
    """Guarda la respuesta cruda + metadatos (evidencia y ejecución offline)."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", encoding="utf-8") as f:
        json.dump({"metadatos": metadatos, "registros": registros}, f, ensure_ascii=False, indent=2)


def cargar_json(ruta: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Carga una respuesta guardada previamente con `guardar_json`."""
    with ruta.open(encoding="utf-8") as f:
        contenido = json.load(f)
    return contenido["registros"], contenido.get("metadatos", {})
