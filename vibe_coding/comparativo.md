# Componente 3 · Vibe Coding: comparación de modelos (20 %)

**Autor:** Juan Diego Varón Valencia · Fundamentos de IA · Universidad de Manizales

## 1. Problema y protocolo

**Problema:** consumir la API pública de Open-Meteo (temperatura horaria de Manizales, últimos 7 días), validar la respuesta, calcular estadísticas básicas y generar una gráfica. Prompt completo en [`promptUtilizado.txt`](promptUtilizado.txt).

| | Local generalista | Local de código | Cloud de código |
|---|---|---|---|
| Modelo | Llama 3.1 8B Instruct (Q4_K_M) | Qwen2.5-Coder 7B Instruct (Q4_K_M) | Claude Sonnet 5 |
| Herramienta | Ollama (`ollama run llama3.1`) | Ollama (`ollama run qwen2.5-coder:7b`) | claude.ai (chat) |
| Respuesta original | [`respuestallama3.1.txt`](respuestallama3.1.txt) | [`respuestaQwen2.5.txt`](respuestaQwen2.5.txt) | [`respuestaSonnet5.txt`](respuestaSonnet5.txt) |
| Código extraído (sin cambios) | [`soluciones/solucion_llama31_8b.py`](soluciones/solucion_llama31_8b.py) | [`soluciones/solucion_qwen25_coder_7b.py`](soluciones/solucion_qwen25_coder_7b.py) | [`soluciones/solucion_claude_sonnet5.py`](soluciones/solucion_claude_sonnet5.py) |
| Fecha de la prueba | 22/09/2026 | 22/09/2026 | 22/09/2026 |

Mismo prompt, una sola vez y sin contexto previo en cada modelo. Cada código se ejecutó **sin modificaciones** para observar qué funciona "tal cual".

**Ciclo de trabajo:** `PROBLEMA → PROMPT → MODELO → CÓDIGO → EJECUCIÓN → ERROR/RESULTADO → CORRECCIÓN → SOLUCIÓN`

## 2. Ciclo observado en cada modelo

**Llama 3.1 8B (local generalista)**
- *Código:* un script lineal sin funciones ni bloque `main`. **No aplicó el tipado estático** que pedía el prompt.
- *Ejecución:* calcula bien las estadísticas y guarda el PNG, pero al final llama a `plt.show()`, que abre una ventana y **deja el script bloqueado** hasta que se cierra.
- *Problemas de diseño:* valida el JSON y los nulos con `assert`, que se desactiva al ejecutar con `python -O`. Envuelve excepciones en `Exception` genérica, así que se pierde el tipo de error.
- *Corrección necesaria:* un segundo prompt pidiendo funciones con tipado, sin `assert` y sin `plt.show()`.

**Qwen2.5-Coder 7B (local de código)**
- *Código:* modular (4 funciones), con tipado (`Dict[str, Any]`) y validaciones HTTP y de llaves con `if`. La llamada principal queda a nivel de módulo, sin `if __name__ == "__main__":`.
- *Error conceptual:* `pd.to_datetime(data['hourly']['time'], unit='s')` y el comentario *"convertimos timestamps UNIX"*. Open-Meteo devuelve fechas **ISO 8601** (`"2026-09-15T00:00"`), no segundos UNIX. Con pandas 3.x el parámetro se ignora y el código funciona; con pandas 2.x esa combinación lanza `ValueError`. El resultado depende de la versión instalada (el computador del autor tiene pandas 3.0.1, así que el script se ejecutará, pero el error conceptual persiste y fallaría en otro equipo con pandas 2.x).
- *Otros detalles:* `marker='o'` sobre más de 300 puntos satura la gráfica, y se lanza `Exception` genérica.

**Claude Sonnet 5 (cloud)**
- *Código:* constantes tipadas, `main()`, docstrings, `timeout` en la petición, excepciones específicas (`RequestException`, `ValueError`, `OSError`) encadenadas con `from`, backend `Agg` para guardar sin ventana y `sys.exit(1)` ante errores.
- *Limitación declarada por el propio modelo:* no pudo probar la llamada real porque su entorno no tenía internet. Lo dijo explícitamente en lugar de asegurar que funcionaba.

**Error que ninguno de los tres detectó (intervención humana).** Al revisar la [documentación de Open-Meteo](https://open-meteo.com/en/docs):
1. El endpoint `/v1/forecast` con `past_days=7` devuelve también **7 días de pronóstico**, porque `forecast_days=7` es el valor por defecto. Las "temperaturas de los últimos 7 días" incluían en realidad 7 días futuros (~336 registros en vez de ~168).
2. Sin el parámetro `timezone`, las horas vienen en **GMT**, 5 horas adelante de Colombia.

**Solución final:** [`soluciones/solucion_final.py`](soluciones/solucion_final.py) toma el código de Claude y añade `forecast_days=0`, `timezone="America/Bogota"` y un filtro que descarta y reporta fechas futuras.

## 3. Matriz comparativa

| Criterio | Local generalista (Llama 3.1 8B) | Local de código (Qwen2.5-Coder 7B) | Cloud de código (Claude Sonnet 5) |
|---|---|---|---|
| **Código ejecutable** | Sí, pero se bloquea en `plt.show()` | Sí con pandas 3.x; falla con pandas 2.x (`unit='s'`) | Sí, sin cambios |
| **Errores encontrados** | Ignoró el tipado; `assert` como validación; `plt.show()` bloqueante | Conversión de fechas conceptualmente errónea; sin bloque `main` | Ninguno de ejecución. Comparte con los otros el error de `forecast_days`/`timezone` |
| **Iteraciones necesarias** | 1–2 (refactor + tipado + quitar `show`) | 1 (corregir `to_datetime` y añadir `main`) | 0 para ejecutar; 1 corrección humana de dominio |
| **Tiempo hasta solución** | Generación: **91.4 s** (762 tokens, 10.0 tokens/s). Más 1–2 iteraciones de corrección de ~1.5 min cada una: **≈ 3–4.5 min** | Generación: **104.7 s** (1 015 tokens, 11.3 tokens/s). Más 1 iteración de corrección: **≈ 3.5 min** | Generación: **≈ 60 s** (cronometrado manualmente, aproximado). Ninguna iteración de código, solo la corrección manual de `forecast_days`/`timezone`: **≈ 1–2 min** |
| **Calidad/claridad del código** | Baja-media: mezcla consumo, validación y gráfica en un solo bloque | Media-alta: funciones con responsabilidad única y tipado | Alta: constantes, docstrings, excepciones específicas |
| **Documentación** | Comentarios numerados por paso | Comentario por bloque + instrucciones de instalación | Docstring de módulo y de funciones + instrucciones |
| **Pruebas sugeridas/generadas** | Ninguna prueba; validaciones con `assert` | Ninguna prueba; validaciones con `if` | Ninguna prueba unitaria; validación de status, JSON, llaves y conteo de nulos |
| **Intervención humana necesaria** | Alta | Media | Baja en código; necesaria en el dominio (API) |

> **Medición de tiempos (27/09/2026):** los tiempos de generación locales se midieron con [`medir_generacion.py`](medir_generacion.py), que envía el mismo `promptUtilizado.txt` a Ollama (datos en `evidence/vibe_coding/tiempos_generacion.csv` y captura `tiempos_generacion_consola.png`). Incluyen ~12 s de carga del modelo en memoria. El tiempo de Claude Sonnet 5 se cronometró a mano en claude.ai. El tiempo por iteración de corrección es una estimación basada en la duración de la primera generación.
>
> **Observación:** aunque Claude Sonnet 5 es un modelo mucho más grande, respondió más rápido (≈ 60 s) que los modelos locales de 7–8B (91–105 s), porque corre en la infraestructura del proveedor. Los modelos locales están limitados por los 4 GB de VRAM del equipo (ver `modelos_locales/registro_tecnico.md`).

> **Pendiente de evidencia:** ejecutar los cuatro scripts de `soluciones/` en el computador del autor y guardar las capturas de consola y los PNG generados en `evidence/vibe_coding/`. La matriz debe apoyarse en esas ejecuciones reales.

## 4. Reflexión técnica

- **La especialización importa más que el tamaño.** Con un tamaño similar (7–8B) y el mismo hardware, el modelo de código siguió las instrucciones de ingeniería (funciones, tipado) que el generalista ignoró.
- **El modelo cloud escribe código más defensivo** (timeouts, excepciones específicas, backend sin ventana) porque anticipa fallos del entorno. También fue el único que dijo con claridad lo que **no** había verificado.
- **Ningún modelo reemplaza la verificación.** Los tres produjeron código que "corre" y los tres respondieron algo distinto de lo pedido (incluían días de pronóstico en horario GMT). El error solo apareció al **leer la documentación de la API y revisar los datos**, no el código. El error de Qwen, además, depende de la versión de pandas, así que "en mi máquina funciona" no basta como prueba.
- **Cambia el rol del desarrollador:** pasa de escribir sintaxis a especificar bien el prompt, revisar, ejecutar, contrastar con la documentación y decidir. La IA acelera la parte mecánica, y la responsabilidad del resultado sigue siendo del desarrollador.
