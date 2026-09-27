# Componente 1 · Cartografía del ecosistema de modelos de IA (20 %)

**Autor:** Juan Diego Varón Valencia · Fundamentos de IA · Universidad de Manizales

**Archivo principal:** [`modelos.csv`](modelos.csv) — 10 modelos en las 6 categorías exigidas (texto/generalista, razonamiento, desarrollo de software, visión/multimodal, voz STT/TTS y embeddings), con una columna **Fuentes** que enlaza la ficha técnica oficial o la página de precios de cada uno.

- **Fecha de verificación de precios y características:** 22-sep-2026. Los precios cloud cambian con frecuencia; hay que volver a consultar la fuente antes de usarlos.
- Para cada categoría se incluyó, cuando existe, **una opción local (open-weight) y una cloud**, porque la decisión depende sobre todo de la privacidad y los recursos.

## Pregunta central: ¿qué modelo usar para cada tipo de problema y por qué?

No hay un "mejor modelo" universal. La elección depende de cinco criterios: **tarea, recursos disponibles, privacidad, costo y modalidad**.

| Problema | Elección | Tarea | Recursos | Privacidad | Costo | Modalidad |
|---|---|---|---|---|---|---|
| Asistente de código con el repositorio de la empresa | **Qwen2.5-Coder 7B** (local) | Generar y explicar código | ~6 GB VRAM o 12 GB RAM: cabe en un portátil | El código no sale del equipo | Gratis | Texto → código |
| Construir una solución completa o depurar un error difícil | **Claude Sonnet 5** (cloud) | Vibe Coding de varios archivos, razonamiento largo | Sin requisitos locales | Aceptable si el código no es confidencial | US$2 / US$10 por 1M tokens | Texto + imágenes |
| Resumir o extraer datos de documentos internos | **Llama 3.1 8B** (local) | Texto general | 16 GB RAM (CPU) o 8 GB VRAM | Datos personales o internos | Gratis | Texto |
| Ejercicios matemáticos o algorítmicos que requieren pasos | **DeepSeek-R1-Distill 14B** (local), o la API de DeepSeek si falta hardware | Razonamiento paso a paso | 12–16 GB VRAM | Local: total | Local gratis; API de bajo costo | Texto |
| Leer capturas, facturas o diagramas | **Qwen2.5-VL 7B** (local) si las imágenes son privadas; **Claude Sonnet 5** si se necesita más precisión | Visión + texto | ~8 GB VRAM (local) | Según el contenido | Gratis / de pago | Imagen + texto |
| Transcribir clases o reuniones en español | **Whisper large-v3** (local) | Voz a texto | ~10 GB VRAM (o *medium* con ~5 GB) | Audio sensible sin salir del equipo | Gratis | Audio → texto |
| Dar voz a una aplicación | **Kokoro-82M** (local, prototipos) / **ElevenLabs** (calidad de producción) | Texto a voz | CPU / ninguno | Local / cloud | Gratis / suscripción | Texto → audio |
| Buscador semántico o RAG sobre apuntes | **bge-m3** (local) si hay privacidad; **text-embedding-3-small** si prima el costo y la simplicidad | Vectorizar texto | 2–4 GB / ninguno | Local / cloud | Gratis / US$0.02 por 1M | Texto → vector |

### Conclusiones

1. **La privacidad decide primero.** Si los datos no pueden salir del equipo, solo sirven modelos open-weight, y entonces el hardware (RAM/VRAM) limita el tamaño a 7–14B cuantizados.
2. **Los recursos definen el tamaño.** Con hardware de estudiante (8–16 GB), los modelos de 7–8B en Q4 funcionan, aunque lentos (en el equipo del autor ~50 s por respuesta, ver Componente 2). Los modelos de más de 70B solo son viables en la nube.
3. **Un modelo especializado pequeño puede superar a uno generalista del mismo tamaño en su tarea.** En el Componente 3, Qwen2.5-Coder 7B estructuró mejor el código que Llama 3.1 8B.
4. **El costo cloud es bajo para un uso puntual**, pero crece con el volumen. Los modelos locales tienen costo marginal cero, pero exigen hardware y tiempo de configuración.
5. **La modalidad filtra antes que la calidad.** Un LLM de texto no transcribe audio. Primero se elige la categoría (STT, VLM, embeddings) y después el modelo.
