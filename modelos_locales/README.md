# Componente 2 · Modelos locales: Ollama + LM Studio (20 %)

**Autor:** Juan Diego Varón Valencia · Fundamentos de IA · Universidad de Manizales

```
MODELO (pesos GGUF Q4_K_M)  ->  OLLAMA / LM STUDIO (runtime)  ->  API LOCAL (HTTP/JSON)  ->  APLICACIÓN PYTHON
llama3.1, qwen2.5-coder:7b      carga el modelo en RAM/VRAM       :11434/api/generate          ollama_test.py
Qwen2.5-Coder-7B-Instruct       y ejecuta la inferencia           :1234/v1/chat/completions    lmstudio_test.py
```

- **Modelo**: el archivo de pesos. No hace nada por sí solo.
- **Runtime/servidor** (Ollama, LM Studio): carga los pesos en memoria, ejecuta la inferencia y publica una API.
- **API local**: contrato HTTP/JSON. Ollama usa su API nativa y LM Studio una API compatible con OpenAI.
- **Aplicación cliente**: el programa Python del laboratorio, que solo conoce la URL y el formato JSON y no depende de dónde corra el modelo.

## Archivos

| Archivo | Propósito |
|---|---|
| `ollama_test.py` | Consume `qwen2.5-coder:7b` vía `POST /api/generate` y mide el tiempo de respuesta. |
| `lmstudio_test.py` | Consume el modelo cargado en LM Studio vía `POST /v1/chat/completions` (formato OpenAI). |
| `comparar_entornos.py` | Envía **las mismas 3 consultas** (general, generar código, explicar código) a Ollama (2 modelos) y a LM Studio, y guarda el tiempo, los tokens/s, la cuantización y la memoria en `evidence/modelos_locales/`. |
| [`registro_tecnico.md`](registro_tecnico.md) | Entorno, modelos, cuantización, memoria y tiempos observados. |

## Ejecución

```bash
# 1. Ollama
ollama --version
ollama pull llama3.1
ollama pull qwen2.5-coder:7b
python ollama_test.py

# 2. LM Studio: descargar Qwen2.5-Coder-7B-Instruct (Q4_K_M), cargarlo
#    y en la pestaña Developer pulsar "Start Server" (puerto 1234)
python lmstudio_test.py

# 3. Comparación equivalente en ambos entornos (con los dos servidores activos)
python comparar_entornos.py
ollama ps     # captura: memoria usada y reparto CPU/GPU del modelo cargado
```
