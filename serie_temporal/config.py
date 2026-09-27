"""Configuración central del reto integrador (Componente 4).

Los valores se leen de variables de entorno (archivo .env opcional) para no
dejar secretos ni rutas fijas dentro del código.
"""
from __future__ import annotations

import os
from datetime import date
from pathlib import Path

try:  # python-dotenv es opcional: si no está instalado se usan las variables del sistema
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # pragma: no cover
    pass

# --- Fuente de datos ---------------------------------------------------------
# Tasa Representativa del Mercado (TRM) USD/COP publicada por la Superintendencia
# Financiera de Colombia en el portal de Datos Abiertos (API Socrata).
# Documentación: https://dev.socrata.com/foundry/www.datos.gov.co/32sa-8pi3
API_URL: str = "https://www.datos.gov.co/resource/32sa-8pi3.json"
DATASET_URL: str = "https://www.datos.gov.co/d/32sa-8pi3"

# Token de aplicación de Socrata. NO es obligatorio (sin él la API funciona con
# un límite de peticiones más bajo). Si se usa, debe ir en .env, nunca en el código.
SOCRATA_APP_TOKEN: str | None = os.getenv("SOCRATA_APP_TOKEN") or None

FECHA_INICIO: str = os.getenv("FECHA_INICIO", "2023-01-01")
FECHA_FIN: str = os.getenv("FECHA_FIN", date.today().isoformat())

REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "30"))
PAGE_SIZE: int = 5000  # registros por página en la paginación de Socrata

# --- Modelado ------------------------------------------------------------------
TEST_SIZE: float = 0.2      # proporción final de la serie reservada para prueba
VENTANA_MEDIA_MOVIL: int = 5  # días hábiles (≈ una semana bursátil)
N_REZAGOS: int = 5          # rezagos (lags) usados por la regresión autorregresiva
HORIZONTE: int = 10         # días hábiles a pronosticar hacia el futuro

# --- Rutas -----------------------------------------------------------------------
BASE_DIR: Path = Path(__file__).resolve().parent
OUTPUT_DIR: Path = BASE_DIR / "outputs"
RAW_JSON_PATH: Path = OUTPUT_DIR / "trm_raw.json"
