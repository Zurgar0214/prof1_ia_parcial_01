# SOLUCIÓN FINAL del Componente 3.
# Base: código de Claude Sonnet 5 (solucion_claude_sonnet5.py), elegido por ser el más robusto.
# Correcciones HUMANAS tras revisar la documentación de Open-Meteo (https://open-meteo.com/en/docs):
#   1. forecast_days=0 -> con solo past_days=7 la API devuelve además 7 días de PRONÓSTICO
#      (forecast_days vale 7 por defecto), así que los "últimos 7 días" incluían datos futuros.
#      Ninguno de los tres modelos detectó esto.
#   2. timezone="America/Bogota" -> por defecto las horas vienen en GMT (5 h de diferencia).
#   3. Validación extra: se descartan (y se reportan) registros con fecha posterior a la hora actual.
"""
Script para consumir la API pública de Open-Meteo y analizar las temperaturas
de los últimos 7 días en Manizales, Colombia.

Requisitos: requests, pandas, matplotlib
"""

from __future__ import annotations

import sys
from typing import Any, Dict

import matplotlib
matplotlib.use("Agg")  # Backend sin interfaz gráfica, apto para guardar archivos
import matplotlib.pyplot as plt
import pandas as pd
import requests

# --- Constantes de configuración ---
LATITUDE: float = 5.0689
LONGITUDE: float = -75.5174
API_URL: str = "https://api.open-meteo.com/v1/forecast"
PAST_DAYS: int = 7
FORECAST_DAYS: int = 0  # [CORRECCIÓN 1] sin días de pronóstico
TIMEZONE: str = "America/Bogota"  # [CORRECCIÓN 2]
OUTPUT_IMAGE: str = "temperatura_manizales.png"
REQUEST_TIMEOUT: int = 15  # segundos


def obtener_datos_clima(latitude: float, longitude: float, past_days: int) -> Dict[str, Any]:
    """
    Realiza la petición GET a la API de Open-Meteo y devuelve el JSON de respuesta.

    Lanza:
        RuntimeError: si el código de estado HTTP no es 200,
                      si la respuesta no es un JSON válido,
                      o si el JSON no contiene las llaves esperadas.
    """
    params: Dict[str, Any] = {
        "latitude": latitude,
        "longitude": longitude,
        "past_days": past_days,
        "hourly": "temperature_2m",
        "forecast_days": FORECAST_DAYS,
        "timezone": TIMEZONE,
    }

    try:
        respuesta: requests.Response = requests.get(
            API_URL, params=params, timeout=REQUEST_TIMEOUT
        )
    except requests.exceptions.RequestException as error:
        # Cubre errores de red, timeout, DNS, etc.
        raise RuntimeError(f"Error de conexión al consultar la API: {error}") from error

    # Validación explícita del código de estado HTTP
    if respuesta.status_code != 200:
        raise RuntimeError(
            f"La API respondió con código HTTP {respuesta.status_code}, se esperaba 200."
        )

    try:
        datos: Dict[str, Any] = respuesta.json()
    except ValueError as error:
        raise RuntimeError("La respuesta de la API no es un JSON válido.") from error

    # Validación de la estructura esperada del JSON
    if "hourly" not in datos:
        raise RuntimeError("El JSON de la respuesta no contiene la llave 'hourly'.")

    if "temperature_2m" not in datos["hourly"]:
        raise RuntimeError(
            "El JSON de la respuesta no contiene la llave 'temperature_2m' dentro de 'hourly'."
        )

    return datos


def construir_dataframe(datos: Dict[str, Any]) -> pd.DataFrame:
    """
    Construye un DataFrame de Pandas a partir del bloque 'hourly' del JSON,
    convirtiendo la columna de fechas a tipo datetime.
    """
    hourly: Dict[str, Any] = datos["hourly"]

    df: pd.DataFrame = pd.DataFrame(
        {
            "fecha": hourly["time"],
            "temperatura": hourly["temperature_2m"],
        }
    )

    # Conversión explícita de la columna de fechas a datetime
    df["fecha"] = pd.to_datetime(df["fecha"], errors="raise")

    # Verificación de valores nulos
    nulos_totales: int = int(df.isnull().sum().sum())
    if nulos_totales > 0:
        print(f"Advertencia: se encontraron {nulos_totales} valores nulos en el DataFrame.")
        print(df.isnull().sum())
    else:
        print("No se encontraron valores nulos en los datos.")

    # [CORRECCIÓN 3] Los datos deben ser solo históricos (hora local de Bogotá)
    ahora = pd.Timestamp.now(tz=TIMEZONE).tz_localize(None)
    futuros = int((df["fecha"] > ahora).sum())
    if futuros:
        print(f"Advertencia: se descartan {futuros} registros con fecha futura (pronóstico).")
        df = df[df["fecha"] <= ahora].reset_index(drop=True)
    print(f"Rango: {df['fecha'].min()} -> {df['fecha'].max()} ({len(df)} registros horarios)")

    return df


def calcular_estadisticas(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calcula media, mediana, mínimo y máximo de la columna 'temperatura'.
    """
    serie_temperatura: pd.Series = df["temperatura"]

    estadisticas: Dict[str, float] = {
        "media": float(serie_temperatura.mean()),
        "mediana": float(serie_temperatura.median()),
        "minimo": float(serie_temperatura.min()),
        "maximo": float(serie_temperatura.max()),
    }
    return estadisticas


def graficar_temperatura(df: pd.DataFrame, ruta_salida: str) -> None:
    """
    Genera una gráfica de línea de la temperatura a lo largo del tiempo
    y la guarda en disco.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df["fecha"], df["temperatura"], color="tab:red", linewidth=1.2)
    plt.title("Temperatura horaria - Manizales (últimos 7 días)")
    plt.xlabel("Fecha y hora")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()

    try:
        plt.savefig(ruta_salida, dpi=150)
    except OSError as error:
        raise RuntimeError(f"No se pudo guardar la imagen en '{ruta_salida}': {error}") from error
    finally:
        plt.close()


def main() -> None:
    """Función principal que orquesta el flujo completo del script."""
    try:
        datos_json: Dict[str, Any] = obtener_datos_clima(LATITUDE, LONGITUDE, PAST_DAYS)
        df_temperatura: pd.DataFrame = construir_dataframe(datos_json)

        estadisticas: Dict[str, float] = calcular_estadisticas(df_temperatura)
        print("\n--- Estadísticas de temperatura (°C) ---")
        print(f"Media:   {estadisticas['media']:.2f}")
        print(f"Mediana: {estadisticas['mediana']:.2f}")
        print(f"Mínimo:  {estadisticas['minimo']:.2f}")
        print(f"Máximo:  {estadisticas['maximo']:.2f}")

        graficar_temperatura(df_temperatura, OUTPUT_IMAGE)
        print(f"\nGráfica guardada exitosamente en '{OUTPUT_IMAGE}'.")

    except RuntimeError as error:
        # Errores controlados (API, validación, guardado de imagen)
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        # Cualquier otro error inesperado
        print(f"Error inesperado: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()