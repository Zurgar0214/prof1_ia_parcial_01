Fundamentos de IA | Laboratorio integrador 

# **PARCIAL 1 - LABORATORIO** 

## **Fundamentos de IA para el Desarrollo** 

## **de Software Aumentado** 

_Comprender - Explorar - Ejecutar - Desarrollar - Construir_ 

|**Curso**|**Fundamentos de I**|**nteligencia Artificial - Ingen**|**iería de Sistemas**||
|---|---|---|---|---|
|**Modalidad**|Equipos de 3 estud|iantes|||
|**Integrantes**|__________________|___________________________|___________||
|**Ponderación**|100 % de la nota de|lparcial / laboratorio|||
|**Propósito**|Usar modelos de I<br>de software.|A como herramientas de aum|entación dentro del ciclo|de vida clásico del desarrollo|
|**1. COMPRENDER**|**2. EXPLORAR**|**3. EJECUTAR**|**4. DESARROLLAR**|**5. CONSTRUIR**|
|**Mapa mental**|**Cartografía**|**Ollama + LM Studio**|**Vibe Coding**|**API + serie temporal**|
|**Reto**<br>**Explorar el ecosist**<br>**conectada a datos**|**ema de modelos de I**<br>**mediante API, conserv**|**A, ejecutar modelos loca**<br>**ando comprensión, verific**|**les y usar IA para desa**<br>**iacióny responsabilida**|**central**<br>**rrollar una solución real**<br>**d humana.**|



### **1. Contexto y propósito del laboratorio** 

Este laboratorio introduce al estudiante en el uso práctico de modelos de Inteligencia Artificial desde la perspectiva del Ingeniero de Sistemas. El objetivo no es utilizar una herramienta de chat de forma aislada, sino comprender qué es un modelo, qué tipos existen, dónde se ejecutan, cómo se integran y cómo pueden aumentar el trabajo del desarrollador 

La ruta parte de los fundamentos conceptuales, continúa con la exploración del ecosistema real de modelos, pasa a la ejecución local con Ollama y LM Studio, experimenta Vibe Coding con diferentes modelos y culmina con una solución de series temporales conectada a una fuente de datos mediante API. 

**Principio rector La IA aumenta al ingeniero: propone, acelera y explica; el estudiante conserva la responsabilidad de comprender, ejecutar, verificar y** **<u>justificar el resultado.</u>** 

### **2. Resultados de aprendizaje** 

- Relacionar los conceptos esenciales de IA, aprendizaje automático, modelos fundacionales y modelos generativos. 

- Distinguir LLM, SLM, VLM, modelos de código, modelos multimodales, STT/TTS y embeddings. 

- Diferenciar modelos locales y cloud, así como modelo, runtime, API y aplicación. 

- Instalar y ejecutar modelos locales con Ollama y LM Studio. 

- Comparar de forma básica modelos generalistas y especializados en desarrollo de software. 

- Aplicar Vibe Coding con supervisión humana para resolver problemas de programación. 

- Construir una aplicación sencilla que consuma una API y procese una serie temporal real. 

- Relacionar el uso de IA con las fases clásicas de requisitos, análisis, diseño, implementación y pruebas. 

### **3. Reglas generales** 

- Toda evidencia debe provenir de ejecuciones reales realizadas por el equipo. 

- Cada equipo debe registrar nombre y versión del modelo utilizado, herramienta de ejecución y fecha de prueba. 

- No se deben publicar API keys, tokens, contraseñas ni secretos en el repositorio. 

- El código generado con IA debe ser ejecutado y comprendido por el equipo; no se acepta código que los integrantes no puedan explicar. 

- Los resultados de comparación deben sustentarse en evidencia observable y no únicamente en percepciones. 

- El repositorio debe conservar código, instrucciones de ejecución y evidencias mínimas del proceso. 

Ingeniería de Sistemas - Desarrollo de Software Aumentado con IA 

Fundamentos de IA | Laboratorio integrador 

### **4. Componente 0 - Mapa mental: Fundamentos de modelos de IA (15 %)** 

Objetivo. Construir una visión integrada de los conceptos que serán utilizados durante el laboratorio. El mapa no debe ser una lista de definiciones aisladas: debe mostrar relaciones, dependencias y ejemplos. 

|**Rama**|**Contenido mínimo**<br>i|
|---|---|
|**Fundamentos**|Inteligencia Artificial, Machine Learning, Deep Learning, redes<br>neuronales,Transformersymodelos fundacionales.|
|**Tipos de modelos**|LLM, SLM, VLM, modelos de código, modelos multimodales,<br>embeddings,Speech-to-TextyText-to-Speech.|
|**Funcionamiento**|Parámetros, tokens, ventana de contexto, inferencia,<br>temperatura,cuantización,entrenamiento vs. inferencia.|
|**Formas de uso**|Modelo local, modelo cloud, API, interfaz de chat, open-weight y<br>modelopropietario.|
|**Infraestructura**|CPU,GPU,RAM,VRAM,Ollama,LM Studioyservicios cloud.|



de calidad. Cada concepto debe responder de forma breve: ¿qué es?, ¿para qué sirve?, un ejemplo y dónde se utilizará en el laboratorio. 

Producto: mapa mental técnico en PDF/PNG o enlace a la herramienta utilizada. 

### **5. Componente 1 - Cartografía del ecosistema de modelos de IA (20 %)** 

Objetivo. Pasar de la definición conceptual al reconocimiento de modelos reales y aprender a seleccionar alternativas de acuerdo con una necesidad concreta. 

El equipo deberá investigar modelos actuales de, al menos, las siguientes categorías: texto/generalistas, razonamiento, desarrollo de software, visión/multimodalidad, voz (STT/TTS) <u>y embeddings.</u> 

|**Modelo**|**Proveedor**|**Tipo**|**Local / Cloud**|**Tamaño**<br> <br>**Contexto**|**/**<br>**Hardware**|**API / Costo**|**Uso**<br>**recomendado**|
|---|---|---|---|---|---|---|---|
|Ejemplo|Organización|LLM / VLM /<br>Coding...|Local / Cloud /<br>ambos|Parámetros<br> <br>contexto|y<br>RAM / VRAM|Disponibilidad|Caso de uso|
|**Pregunta**|||||||**central**|



**¿Qué modelo utilizaría para cada tipo de problema y por qué? La conclusión debe considerar tarea, recursos,** **<u>privacidad, costo y modalidad, no declarar un “mejor modelo” universal.</u>** 

Producto: matriz comparativa con fuentes técnicas u oficiales que permitan verificar las características reportadas. 

### **6. Componente 2 - Laboratorio de modelos locales: Ollama + LM Studio (20 %)** 

Objetivo. Instalar, ejecutar y consumir modelos de IA localmente, diferenciando con claridad modelo, runtime/servidor, API y aplicación cliente. 

#### **6.1 Actividades obligatorias** 

1. Instalar Ollama y verificar su funcionamiento. 

2. Descargar y ejecutar un modelo generalista adecuado al hardware disponible. 

3. Descargar y ejecutar un modelo orientado a programación. 

4. Instalar LM Studio y ejecutar al menos un modelo compatible. 

5. Realizar un conjunto equivalente de consultas en ambos entornos. 

6. Registrar modelo, cuantización cuando aplique, RAM/VRAM observada y tiempo aproximado de respuesta. 

7. Consumir al menos un modelo desde un programa Python mediante una API local. 

**Relación que debe poder explicar el estudiante** 

**MODELO -> OLLAMA / LM STUDIO -> API LOCAL -> APLICACIÓN PYTHON** 

#### **6.2 Evidencia mínima** 

|**Evidencia**|**Qué demostrar**|
|---|---|
|**Instalación**|OllamayLM Studio funcionando en el equipo.|
|**Modelogeneralista**|Cargayrespuesta real.|
|**Modelo de código**|Generación o explicación de código.|
|**Recursos**|Registro básico de RAM/VRAMytiempo de respuesta.|



Ingeniería de Sistemas - Desarrollo de Software Aumentado con IA 

||Fundamentos de IA | Laboratorio integrador|
|---|---|
|**Evidencia**|**Qué demostrar**|
|**API local**|Programa Python que envía una solicitud y recibe una respuesta<br>del modelo.|



Producto: evidencia de ejecución + programa Python consumidor de IA local + breve registro técnico del entorno utilizado. 

### **7. Componente 3 - Práctica de Vibe Coding: comparación de modelos (20 %)** 

Objetivo. Experimentar cómo cambia el desarrollo de software cuando se utiliza un modelo generalista, un modelo especializado en código y un modelo avanzado de desarrollo disponible en la nube. 

El docente propondrá un mismo problema de programación para todos los modelos. El problema debe ser pequeño y verificable, por ejemplo: consumir una API pública, validar la respuesta, calcular estadísticas básicas y generar una visualización. 

#### **7.1 Comparación mínima** 

- Modelo local generalista. 

- Modelo local especializado en código. 

- Modelo de desarrollo cloud, <u>por ejemplo Codex o equivalente disponible para el equipo.</u> 

|**Criterio**|**Localgeneral**||**Local coding**|**Cloud coding**|
|---|---|---|---|---|
|**Código ejecutable**|||||
|**Errores encontrados**|||||
|**Iteraciones necesarias**|||||
|**Tiempo hasta solución**|||||
|**Calidad/claridad del código**|||||
|**Documentación**|||||
|**Pruebas sugeridas/generadas**|||||
|**Intervención humana necesaria**|||||
|**Ciclo**||**de**||**trabajo**|



##### **PROBLEMA -> PROMPT -> MODELO -> CÓDIGO -> EJECUCIÓN -> ERROR/RESULTADO -> CORRECCIÓN -> SOLUCIÓN** 

Producto: solución ejecutable, tabla comparativa y reflexión técnica breve sobre qué cambió al utilizar modelos diferentes. 

### **8. Componente 4 - Reto integrador: Vibe Coding + API + Series Temporales (25 %)** 

Objetivo. Integrar lo aprendido en una aplicación sencilla construida con apoyo de IA que consuma datos reales desde una API pública y resuelva un problema básico de series temporales. 

#### **8.1 Reto** 

Construir una aplicación en Python que obtenga datos históricos desde una API pública, prepare una serie temporal, genere visualizaciones y produzca una predicción sencilla. El equipo puede utilizar una API meteorológica, financiera, energética u otra fuente pública aprobada por el docente. 

#### **8.2 Requisitos mínimos** 

- Conectarse a una API pública y obtener datos reales en formato JSON u otro formato documentado. 

- Convertir la respuesta en una estructura analizable con Python/Pandas. 

- Validar tipos de datos, fechas, valores faltantes y orden temporal. 

- Construir y visualizar al menos una serie temporal. 

- Implementar un baseline sencillo (por ejemplo persistencia o media móvil). 

- Implementar un método predictivo básico apropiado para el nivel del curso. 

- Separar datos de entrenamiento y prueba respetando el orden temporal; no utilizar información futura para predecir el pasado. 

- Comparar valores reales vs. predicción y calcular al menos MAE y RMSE. 

- Documentar cómo fue utilizada la IA durante el desarrollo y qué decisiones fueron tomadas por el equipo. 

#### **8.3 Relación con el ciclo de vida clásico del software** 

|**Fase**|**Aplicación mínima en el reto**<br>i|
|---|---|
|**Requisitos**|Definir qué datos necesita la aplicación, qué debe mostrar y qué<br>debepredecir.|
|**Análisis**|Revisar la API,estructura de datos,variablesyrestricciones.|
|**Diseño**|Definir módulos o flujo básico de la solución.|
|**Implementación**|Desarrollar la aplicación con apoyo de Vibe Coding.|
|**Pruebas**|Ejecutar,validar datos,revisar erroresycomprobar|



Ingeniería de Sistemas - Desarrollo de Software Aumentado con IA 

Fundamentos de IA | Laboratorio integrador 

|**Fase**|**Aplicación mínima en el reto**<br>métricas/resultados.|
|---|---|



|**Flujo**<br>**esperado**|
|---|
|**API -> JSON/DATOS -> PYTHON/PANDAS -> PREPARACIÓN -> SERIE TEMPORAL -> MODELO -> PREDICCIÓN ->**|
|**MAE/RMSE -> GRÁFICAS**|



Producto: aplicación funcional + código fuente + evidencia de consumo de API + gráficas + métricas + documentación breve del proceso. 

### **9. Entregables obligatorios** 

- Mapa mental técnico de fundamentos. 

- Matriz de cartografía del ecosistema de modelos. 

- Evidencia de Ollama y LM Studio funcionando. 

- Programa Python que consuma un modelo local mediante API. 

- Comparativo de Vibe Coding usando los tres tipos de modelo definidos. 

- Aplicación integradora de series temporales conectada a una API pública. 

- Repositorio Git con README, código fuente, requirements.txt y .env.example cuando aplique. 

- Carpeta de evidencias con capturas o registros mínimos de las ejecuciones. 

- Presentación o video corto de demostración según indicación del docente. 

### **10. Estructura mínima sugerida del repositorio** 

```
/fundamentos-ia-lab
```

- `├── README.md ├── requirements.txt ├── .env.example ├── /mapa_mental ├── /cartografia_modelos │   └── modelos.csv ├── /modelos_locales │   ├── ollama_test.py │   └── lmstudio_test.py ├── /vibe_coding │   └── comparativo.md ├── /serie_temporal │   ├── api_client.py │   ├── preprocessing.py │   ├── model.py │   ├── evaluation.py │   └── app.py ├── /tests └── /evidence` 

### **11. Rúbrica de evaluación** 

|**Criterio**|**Peso**|**Excelente(4.5-5.0)**|**Competente(3.5-4.4)**|**Insuficiente(0.0-3.4)**|
|---|---|---|---|---|
|**1. Mapa mental**|15 %|Relacional,<br>claro,<br>con<br>conceptos,<br>ejemplos<br>y<br>conexiones correctas.|Incluye conceptos principales<br>pero con relaciones o<br>ejemplos limitados.|Lista superficial, incompleta<br>o con errores conceptuales.|
|**2. Cartografía de modelos**|20 %|Matriz completa, fuentes<br>verificables y selección<br>argumentada<br>por<br>tarea/restricción.|Comparación válida pero<br>parcial<br>o<br>con<br>poca<br>justificación.|Información no verificable,<br>desactualizada<br>o<br>comparación subjetiva.|
|**3. Ollama + LM Studio**|20 %|Ambos entornos funcionan;<br>modelos ejecutados; API<br>local integrada y recursos<br>documentados.|Ejecución parcial o API<br>incompleta.|No logra ejecutar modelos<br>localmente o no presenta<br>evidencia.|
|**4. Vibe Coding**|20 %|Tres enfoques comparados<br>con la misma tarea,<br>evidencia,<br>ejecución<br>y<br>análisis técnico.|Comparación incompleta o<br>con poca evidencia.|Conclusiones subjetivas o<br>soluciones no ejecutables.|
|**5. Reto integrador**|25 %|API real, serie temporal<br>correcta, baseline/modelo,<br>métricas, gráficas y proceso<br>reproducible.|Solución funcional con<br>elementos o evidencias<br>incompletos.|No integra datos reales,<br>predicción o métricas de<br>forma válida.|



### **12. Condiciones mínimas de aprobación** 

- El equipo debe demostrar que al menos un modelo local funciona en su entorno. 

- Debe existir consumo programático de un modelo mediante API local. 

- La práctica de Vibe Coding debe producir código que pueda ejecutarse y verificarse. 

- El reto integrador debe consumir datos reales desde una API y respetar el orden temporal de los datos. 

Ingeniería de Sistemas - Desarrollo de Software Aumentado con IA 

Fundamentos de IA | Laboratorio integrador 

 No se aceptan secretos publicados en el repositorio. 

- El equipo debe poder explicar el código y las decisiones realizadas con ayuda de IA. 

- **Cierre esperado El estudiante pasa de “usar una IA” a comprender qué modelo utiliza, dónde se ejecuta, cómo se integra y cómo** **<u>puede aumentar el desarrollo de una solución de software real.</u>** 

Ingeniería de Sistemas - Desarrollo de Software Aumentado con IA 

