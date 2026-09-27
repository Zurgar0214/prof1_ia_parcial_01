# Registro técnico del entorno · Componente 2

> Los datos marcados con ✅ se tomaron de las capturas y registros en `evidence/`.

## Equipo de prueba

**Responsable de las pruebas:** Juan Diego Varón Valencia

| Campo | Valor |
|---|---|
| Fechas de las pruebas | 22/09/2026 (instalación y `ollama_test.py`) · 27/09/2026 (LM Studio y `comparar_entornos.py`) ✅ |
| Equipo | ASUS TUF Dash F15 (FX517ZC) ✅ `evidence/entorno/dxdiag_sistema.png` |
| Sistema operativo | Windows 11 Home Single Language 64 bits, compilación 26200 ✅ |
| CPU | Intel Core i5-12450H (12.ª gen., 8 núcleos: 4 de rendimiento + 4 de eficiencia, 12 hilos) ✅ |
| RAM total | 32 GB (32 768 MB) ✅ |
| GPU / VRAM | NVIDIA GeForce RTX 3050 Laptop, 4 GB VRAM (configuración del modelo FX517ZC; confirmar en DxDiag → pestaña *Pantalla 2*) |
| Python | 3.13.5 ✅ |
| Ollama | 0.34.4 ✅ `evidence/ollama/ollama_version.png` |
| LM Studio | 0.4.25 ✅ (título de la ventana) |

## Modelos ejecutados

| Entorno | Modelo | Tipo | Parámetros | Cuantización | Tamaño en disco | Evidencia |
|---|---|---|---|---|---|---|
| Ollama | `llama3.1` (8B Instruct) | Generalista | 8B | Q4_K_M (predeterminada de Ollama) | 4.9 GB ✅ | `evidence/ollama/ollama_model_installation.png` |
| Ollama | `qwen2.5-coder:7b` | Código | 7.6B | Q4_K_M | 4.7 GB ✅ | `evidence/ollama/ollama_model_installation.png` |
| LM Studio | `Qwen2.5-Coder-7B-Instruct-GGUF` (lmstudio-community) | Código | 7.6B | Q4_K_M ✅ | 4.68 GB ✅ | `evidence/lmstudio/model_installation.png` |

## Recursos y tiempos observados

Las mismas 3 consultas se enviaron a los tres entornos con `comparar_entornos.py` (temperatura 0.2) el 27/09/2026. Datos crudos en [`evidence/modelos_locales/resultados_entornos.csv`](../evidence/modelos_locales/resultados_entornos.csv) y respuestas completas en [`respuestas_entornos.md`](../evidence/modelos_locales/respuestas_entornos.md).

| Entorno · modelo | Consulta | Tiempo total (s) | Carga del modelo (s) | Tokens generados | Tokens/s |
|---|---|---|---|---|---|
| Ollama · llama3.1 (8B) | general | 23.17 | 12.84 | 90 | 11.41 |
| Ollama · llama3.1 (8B) | codigo_generar | 57.49 | 0.01 | 541 | 9.82 |
| Ollama · llama3.1 (8B) | codigo_explicar | 52.16 | 0.01 | 471 | 9.46 |
| Ollama · qwen2.5-coder:7b | general | 22.27 | 12.20 | 106 | 13.80 |
| Ollama · qwen2.5-coder:7b | codigo_generar | 52.26 | 0.01 | 630 | 12.70 |
| Ollama · qwen2.5-coder:7b | codigo_explicar | 42.88 | 0.01 | 521 | 12.97 |
| LM Studio · Qwen2.5-Coder 7B Q4_K_M | general | 14.65 | (ya cargado) | 115 | 7.85* |
| LM Studio · Qwen2.5-Coder 7B Q4_K_M | codigo_generar | 48.76 | (ya cargado) | 578 | 11.85* |
| LM Studio · Qwen2.5-Coder 7B Q4_K_M | codigo_explicar | 58.27 | (ya cargado) | 681 | 11.69* |
| Ollama · qwen2.5-coder:7b | Media móvil (`ollama_test.py`, 22/09) | 53.70 ✅ | — | — | — |

**Configuración de carga en LM Studio** (`evidence/lmstudio/lmstudio_config_carga.png`): contexto 8 192 tokens (el modelo admite hasta 32 768), **GPU Offload 16 capas** (Qwen2.5-7B tiene 28), 4 hilos de CPU, Flash Attention activado, caché KV en la GPU, *Keep Model in Memory* y *mmap* activados. LM Studio no muestra en esta vista los GB exactos de RAM/VRAM usados; el reparto se expresa en capas.

\* En LM Studio los tokens/s se calculan sobre el tiempo total (incluye el procesamiento del prompt); en Ollama sobre el tiempo de generación que reporta el servidor. Por eso la cifra de LM Studio en la consulta corta sale más baja.

**Memoria observada (Ollama `/api/ps`, modelo cargado):**

| Modelo | Memoria total del modelo | En VRAM (GPU) | En RAM (CPU) | Reparto aprox. |
|---|---|---|---|---|
| llama3.1 8B Q4_K_M | 5.61 GB | 2.06 GB | 3.55 GB | 37 % GPU / 63 % CPU |
| qwen2.5-coder:7b Q4_K_M | 5.12 GB | 2.28 GB | 2.84 GB | 45 % GPU / 55 % CPU |
| LM Studio · Qwen2.5-Coder 7B | 4.68 GB ✅ | 16 de 28 capas en GPU + caché KV en GPU | 12 capas en CPU | ≈ 57 % GPU / 43 % CPU (por capas) |

## Análisis de los resultados

1. **Descarga parcial a GPU.** Con 4 GB de VRAM, ninguno de los dos modelos (5.1–5.6 GB cargados) cabe completo en la GPU: solo 2.1–2.3 GB van a la VRAM (el resto de la VRAM lo ocupan el contexto y Windows) y el resto corre en la CPU usando la RAM. Los 32 GB de RAM permiten cargar el modelo sin problema; el cuello de botella es la VRAM. Eso explica la velocidad de ~9–14 tokens/s y respuestas de 40–60 s para código. Coincide con el aviso *"Partial GPU Offload Possible"* de LM Studio.
2. **Tiempo de carga.** La primera consulta de cada modelo en Ollama incluye ~12–13 s de carga en memoria; las siguientes, ~0 s, porque el modelo queda residente.
3. **Modelo más pequeño, más rápido.** Qwen2.5-Coder (7.6B) generó ~30 % más tokens/s que Llama 3.1 (8B): 12.7–13.8 frente a 9.5–11.4. Ocupa menos memoria y una mayor proporción queda en la GPU (45 % frente a 37 %).
4. **Mismo modelo, dos runtimes.** Qwen2.5-Coder 7B Q4_K_M rindió parecido en Ollama y LM Studio en respuestas largas (~12–13 frente a ~11.7–11.9 tokens/s). El runtime cambia poco el rendimiento cuando el modelo y la cuantización son los mismos; lo que domina es el hardware.
5. **Calidad (consulta `codigo_explicar`).** El código de prueba tiene un error real: `range(len(xs))` en lugar de `range(len(xs) - k + 1)`, por lo que las últimas `k−1` "medias" se calculan con menos de `k` elementos pero divididas por `k`. Ningún modelo lo explicó bien:
   - **Llama 3.1** dijo que habría un error de índice (falso: en Python el *slicing* no lanza `IndexError`), pero su corrección sí cambió el rango correctamente.
   - **Qwen2.5-Coder (Ollama)** también afirmó que habría `IndexError` y su "corrección" **mantuvo el error** del rango.
   - **Qwen2.5-Coder (LM Studio)** explicó bien que el *slicing* no falla, pero su ejemplo omitió el último valor (`f([1,2,3,4,5], 2)` devuelve `[1.5, 2.5, 3.5, 4.5, 2.5]`, no `[1.5, 2.5, 3.5, 4.5]`).

   Conclusión sobre la calidad: incluso en una tarea de 2 líneas, las respuestas de modelos locales pequeños deben verificarse **ejecutando el código**, no por la explicación.

6. **Configuración vs. rendimiento.** LM Studio envió más capas a la GPU (57 %) que Ollama (≈45 % de la memoria de Qwen), pero con solo 4 hilos de CPU para las 12 capas restantes. El resultado fue un rendimiento similar (~11.7 frente a ~12.9 tokens/s en respuestas largas). Aumentar *CPU Thread Pool Size* a 8 (los núcleos del i5-12450H) o reducir el contexto para liberar VRAM y subir el *GPU Offload* son ajustes posibles para acelerar la inferencia.

## Evidencia (checklist)

- [x] Captura de LM Studio con el modelo cargado (READY), servidor activo en `127.0.0.1:1234` y `lmstudio_test.py` respondiendo (`evidence/lmstudio/lmStudio_evidence.png`).
- [x] Modelo generalista respondiendo: llama3.1 contestó las 3 consultas vía API (`respuestas_entornos.md`). Opcional: captura de `ollama run llama3.1`.
- [x] Memoria por modelo registrada vía `/api/ps` de Ollama (`resultados_entornos.csv`) y configuración de carga de LM Studio (`lmstudio_config_carga.png`).
- [x] `evidence/modelos_locales/resultados_entornos.csv` generado con `comparar_entornos.py` (27/09/2026).
