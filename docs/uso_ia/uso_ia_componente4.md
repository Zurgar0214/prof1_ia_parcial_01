# Uso de IA en el desarrollo · Componente 4

| Campo | Valor |
|---|---|
| Autor / responsable | Juan Diego Varón Valencia |
| Herramienta | Claude (Cowork, app de escritorio), agente con acceso a la carpeta del proyecto |
| Modelo | Identificador configurado en la sesión: `claude-opus-5-5` |
| Fecha | 22-sep-2026 |
| Insumos entregados a la IA | Enunciado del laboratorio (`docs/enunciado_laboratorio.md`) y los componentes 0–3 ya elaborados |

## Qué hizo la IA

1. **Revisión de lo existente** frente al enunciado y la rúbrica, con una lista de pendientes por componente.
2. **Verificación de la API** antes de escribir código: consultó el endpoint real de la TRM y confirmó los nombres de campos, que los valores llegan como texto y el formato de las vigencias (5 registros reales que hoy se usan en las pruebas).
3. **Generación del código** de `serie_temporal/` (5 módulos + `config.py`) y de `tests/` (20 pruebas iniciales; 21 tras la corrección del 27-sep).
4. **Ejecución de las pruebas** en su entorno: 20/20 correctas. También ejecutó el flujo completo con una serie **sintética** porque su entorno no tenía salida de red a la API. Esos datos simulados **no** se incluyen como evidencia.
5. **Documentación**: README del componente y este registro.

## Prompts principales (resumen)

- "Revisa lo que tengo pendiente, completa el componente 4 y complementa lo necesario para cumplir con lo solicitado y con buena calidad."
- Elección de la fuente de datos: se pidió una fuente **financiera (cripto/divisas)**. La IA propuso la TRM de Datos Abiertos Colombia y el autor la aceptó.
- Reorganización de carpetas según la estructura sugerida en la sección 10 del enunciado.

## Decisiones: quién decidió qué

| Decisión | Propuesta por | Validación del autor |
|---|---|---|
| Dominio financiero (divisas) | Juan Diego Varón Valencia | — |
| Fuente: TRM de datos.gov.co, sin API key | IA | Aceptada: fuente oficial, pública y sin credenciales |
| Una observación por día hábil (no expandir a días calendario) | IA | Aceptada: repetir valores de fin de semana haría acertar a la persistencia "gratis" |
| Baselines: persistencia y media móvil de 5 días | IA (el enunciado sugiere ambas) | Aceptada |
| Modelo: regresión lineal AR(5) con scikit-learn | IA | Aceptada: interpretable y adecuada al nivel del curso |
| Split temporal 80/20 + validación walk-forward | IA (lo exige el enunciado) | Aceptada |
| Estructura modular según el enunciado | Enunciado | — |

## Verificación humana requerida (checklist del autor)

El enunciado exige que el estudiante pueda **explicar** el código generado con IA. Antes de entregar:

- [x] Ejecutar `python -m pytest -v` en el computador del autor (`evidence/serie_temporal/test_passed.png`).
- [x] Ejecutar `python app.py` con conexión a internet (27-sep-2026: HTTP 200, 881 registros). Capturas: `evidence/serie_temporal/ejecucion_serie_temporal.png` (en línea, antes de corregir las fechas) y `ejecucion_offline.png` (con la corrección).
- [x] Revisar las 4 gráficas y copiar la tabla de métricas real en `serie_temporal/README.md`.
- [x] El autor revisó y puede explicar:
  - [x] por qué `shift(1)` evita usar información futura en la media móvil y en los rezagos;
  - [x] por qué el split no puede ser aleatorio en una serie temporal;
  - [x] la diferencia entre MAE y RMSE y por qué el RMSE es siempre ≥ MAE;
  - [x] por qué la persistencia es tan difícil de superar en una tasa de cambio;
  - [x] qué valida `preprocessing.a_dataframe` (tipos, faltantes, duplicados, orden, vigencias).
- [x] Anotar aquí cualquier error encontrado al ejecutar en Windows y cómo se corrigió (ciclo `ERROR → CORRECCIÓN`).

## Errores y correcciones durante el desarrollo

| # | Situación | Corrección |
|---|---|---|
| 1 | La IA no pudo acceder a la API desde su entorno (red bloqueada) | Probó con registros reales obtenidos por otra vía y con datos sintéticos. La ejecución real contra la API la hace el autor. |
| 2 | `pytest` no estaba disponible en el entorno de la IA | Ejecutó las pruebas con un ejecutor mínimo equivalente. El autor debe correrlas con `pytest` real. |
| 3 | Al revisar la ejecución real (27-sep), el pronóstico futuro empezaba el lunes 28-sep, pero ese día ya estaba cubierto por la TRM del sábado 26 (`vigenciahasta` = 28-sep). Además usaba días lunes-viernes, mientras que las vigencias reales empiezan de martes a sábado (conteo en `trm_raw.json`: 0 lunes, 185 sábados). | El pronóstico ahora empieza el día siguiente a la última `vigenciahasta` y usa el calendario martes-sábado. Se añadió la prueba `test_pronostico_futuro_con_fechas_de_vigencia`. Las métricas no cambian (solo afecta las fechas del pronóstico futuro). |
| 4 | Al ejecutar `python -m pytest -v` se recolectaron 23 pruebas en lugar de 21: pytest también tomó `modelos_locales/ollama_test.py` y `lmstudio_test.py` (su patrón por defecto incluye `*_test.py`), que llaman a Ollama y LM Studio. Por eso la ejecución tardó 96 s. | Se añadió `pytest.ini` con `testpaths = tests`: ahora solo corren las 21 pruebas del Componente 4, en pocos segundos y sin depender de los servidores locales. |
