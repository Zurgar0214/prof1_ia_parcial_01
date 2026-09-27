# Fundamentos de IA para el Desarrollo de Software Aumentado · Parcial 1 (Laboratorio)

**Curso:** Profundización IA I · Ingeniería de Sistemas · Universidad de Manizales
**Autor:** Juan Diego Varón Valencia

> *La IA aumenta al ingeniero: propone, acelera y explica; el estudiante conserva la responsabilidad de comprender, ejecutar, verificar y justificar el resultado.*

Enunciado completo: [`docs/enunciado_laboratorio.md`](docs/enunciado_laboratorio.md)

## Mapa del repositorio

| Componente | Peso | Carpeta | Entregable principal |
|---|---|---|---|
| 0 · Mapa mental | 15 % | [`mapa_mental/`](mapa_mental/) | `mapamental.png` (jerarquía) + `relaciones.png` (conexiones) |
| 1 · Cartografía de modelos | 20 % | [`cartografia_modelos/`](cartografia_modelos/) | `modelos.csv` con fuentes + conclusión por tarea y restricción |
| 2 · Ollama + LM Studio | 20 % | [`modelos_locales/`](modelos_locales/) | `ollama_test.py`, `lmstudio_test.py`, `comparar_entornos.py`, `registro_tecnico.md` |
| 3 · Vibe Coding | 20 % | [`vibe_coding/`](vibe_coding/) | `comparativo.md` + código de los 3 modelos + `soluciones/solucion_final.py` |
| 4 · Reto integrador | 25 % | [`serie_temporal/`](serie_temporal/) | App de pronóstico de la TRM USD/COP (API → Pandas → modelo → MAE/RMSE → gráficas) |
| Evidencias | — | [`evidence/`](evidence/) | Capturas y registros de las ejecuciones |
| Pruebas | — | [`tests/`](tests/) | 21 pruebas `pytest` del Componente 4 |
| Uso de IA | — | [`docs/uso_ia/`](docs/uso_ia/) | Conversación con Gemini (C0–C3) y registro de uso de Claude (C4) |

```
├── README.md · requirements.txt · .env.example · .gitignore · pytest.ini
├── mapa_mental/            mapamental.puml/.png · relaciones.mmd/.png
├── cartografia_modelos/    modelos.csv · README.md
├── modelos_locales/        ollama_test.py · lmstudio_test.py · comparar_entornos.py · registro_tecnico.md
├── vibe_coding/            comparativo.md · promptUtilizado.txt · respuesta*.txt · soluciones/
├── serie_temporal/         config.py · api_client.py · preprocessing.py · model.py · evaluation.py · app.py · outputs/
├── tests/                  test_api_client.py · test_preprocessing.py · test_model_evaluation.py
├── evidence/               ollama/ · lmstudio/ · modelos_locales/ · vibe_coding/ · serie_temporal/
└── docs/                   enunciado_laboratorio.md · uso_ia/
```

## Instalación

```bash
git clone <url-del-repositorio>
cd <repositorio>
python -m venv .venv
# Windows:   .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # opcional: ningún componente requiere API key
```

## Ejecución rápida

```bash
# Componente 2 (con Ollama y/o LM Studio corriendo)
python modelos_locales/ollama_test.py
python modelos_locales/lmstudio_test.py
python modelos_locales/comparar_entornos.py

# Componente 3
python vibe_coding/soluciones/solucion_final.py

# Componente 4
cd serie_temporal && python app.py && cd ..
python -m pytest -q
```

## Modelos y herramientas utilizados

| Uso | Modelo | Herramienta | Local/Cloud | Fecha |
|---|---|---|---|---|
| Elaboración de C0–C3 | Gemini | gemini.google.com | Cloud | 22-sep-2026 |
| Modelo local generalista (C2, C3) | Llama 3.1 8B Instruct Q4_K_M | Ollama | Local | 22 y 27-sep-2026 |
| Modelo local de código (C2, C3) | Qwen2.5-Coder 7B Instruct Q4_K_M | Ollama y LM Studio 0.4.25 | Local | 22 y 27-sep-2026 |
| Modelo cloud de código (C3) | Claude Sonnet 5 | claude.ai | Cloud | 22-sep-2026 |
| Desarrollo de C4 y revisión del repositorio | Claude (`claude-opus-5-5`) | Claude Cowork | Cloud | 22 y 27-sep-2026 |

## Seguridad
- No hay API keys, tokens ni contraseñas en el repositorio. `.env` está en `.gitignore`, y el único secreto opcional (`SOCRATA_APP_TOKEN`) se lee desde variables de entorno.
- Las APIs usadas (Open-Meteo, Datos Abiertos Colombia) son públicas y no requieren autenticación.
