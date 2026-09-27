# Evidencias de ejecución

Todas las evidencias deben provenir de ejecuciones reales realizadas por el autor, Juan Diego Varón Valencia (regla 1 del enunciado).

| Carpeta | Contenido | Estado |
|---|---|---|
| `entorno/` | `dxdiag_sistema.png`: especificaciones del computador (i5-12450H, 32 GB RAM, Windows 11) | ✅ |
| `ollama/` | Descarga de `llama3.1` y `qwen2.5-coder:7b`; `ollama_test.py` respondiendo en 53.70 s | ✅ |
| `lmstudio/` | Descarga de Qwen2.5-Coder-7B-Instruct Q4_K_M | ✅ |
| `ollama/` | `ollama_version.png`: Ollama 0.34.4 | ✅ |
| `lmstudio/` | `lmstudio_servidor_modelo.png` y `lmstudio_config_carga.png`: modelo Q4_K_M cargado, servidor activo, contexto 8 192, 16 capas en GPU | ✅ |
| `lmstudio/` | `lmStudio_evidence.png`: modelo cargado (READY), servidor en :1234 y `lmstudio_test.py` respondiendo | ✅ |
| `modelos_locales/` | `resultados_entornos.csv` y `respuestas_entornos.md` (27-sep-2026) | ✅ |
| `vibe_coding/` | `tiempos_generacion.csv`, respuestas regeneradas y `tiempos_generacion_consola.png` (27-sep-2026) | ✅ |
| `serie_temporal/` | `test_passed.png` (pytest), `ejecucion_serie_temporal.png` (en línea, HTTP 200) y `ejecucion_offline.png` (con la corrección de fechas); resultados en `serie_temporal/outputs/` | ✅ |

Las gráficas, métricas y el JSON crudo del Componente 4 se generan en `serie_temporal/outputs/` y también cuentan como evidencia.
