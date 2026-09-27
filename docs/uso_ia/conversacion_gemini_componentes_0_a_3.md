

Laboratorio_F undamentos_ IA_Desarroll… 

Ayúdame a elaborar desde el componente 0 al 3... Cómo considerarías un plan ordenado de ejecución y una estrategia para lograr y cumplir con los entregables 

Para abordar los entregables de este laboratorio de manera ordenada y estratégica, le sugiero un plan de ejecución dividido en fases. Su experiencia estructurando arquitecturas backend, consumiendo APIs y gestionando repositorios con herramientas Git le será de gran utilidad para organizar este flujo de trabajo. A continuación, le presento una propuesta de plan y estrategia para resolver del Componente 0 al 3: 

### Fase 1: Preparación del Entorno y Estructura (Semana 1) 

Antes de ejecutar los modelos, es vital establecer la base del proyecto. 

- Configuración del repositorio: Inicialice un repositorio Git creando la estructura de 

- carpetas sugerida, incluyendo directorios como /mapa_mental , /cartografia_modelos , /modelos_locales y /vibe_coding . 

- MD 

- Gestión de dependencias: Cree el archivo requirements.txt y el .env.example para asegurar que las credenciales no se expongan en el código. 

- MD 

- Reglas de trabajo: Establezca desde el inicio que todo el código generado por IA debe ser comprendido y ejecutable por el equipo. No se aceptará código que no pueda ser explicado. 

- MD + 1 

### Fase 2: Fundamentación Teórica (Componentes 0 y 1) 

Esta fase se centra en la investigación y conceptualización. 

#### Componente 0 - Mapa mental (15%): 

   - El objetivo es construir una visión integrada de los conceptos de IA. MD 

   - El mapa debe evidenciar relaciones, dependencias y ejemplos, evitando ser una simple lista de definiciones. 

   - MD 

   - Debe abarcar cinco ramas mínimas: fundamentos (Machine Learning, redes neuronales, Transformers), tipos de modelos (LLM, SLM, embeddings), funcionamiento (parámetros, tokens, cuantización), formas de uso (API, local, cloud) e infraestructura (CPU, GPU, RAM). 

   - MD 

   - Estrategia: Utilice herramientas de diagramación para conectar cómo la infraestructura y los parámetros afectan el rendimiento en los despliegues locales versus la nube. 

- Componente 1 - Cartografía del ecosistema (20%): 

   - Deberá investigar modelos actuales y construir una matriz comparativa. 

   - MD 

   - La matriz debe incluir categorías como texto/generalistas, razonamiento, desarrollo de software, visión, voz (STT/TTS) y embeddings. 

   - MD 

   - Para cada modelo, registre el proveedor, tipo, modalidad (local/cloud), tamaño/contexto, hardware requerido, API/costo y el uso recomendado. 

   - MD 

   - Estrategia: Evalúe los modelos desde una perspectiva arquitectónica. Considere qué modelo utilizaría según la privacidad, los recursos y el costo, evitando declarar un "mejor modelo" universal. 

   - MD 

### Fase 3: Ejecución Local e Integración (Componente 2) 

Aquí pondrá en práctica la infraestructura local. 

Componente 2 - Ollama + LM Studio (20%): 

- Deberá instalar Ollama y LM Studio en su equipo. 

- MD 

- Es obligatorio descargar y ejecutar un modelo generalista y otro orientado a programación. 

- MD 

- Debe registrar el nombre del modelo, la cuantización, la RAM/VRAM observada y el tiempo aproximado de respuesta. 

- MD 

- Se requiere consumir al menos un modelo local desde un programa en Python a través de una API. MD 

Estrategia: Dado su manejo de Python y validación de endpoints, levante el servidor de Ollama o LM Studio y pruebe las respuestas primero con herramientas de testeo de APIs. Luego, escriba los scripts ollama_test.py y lmstudio_test.py para automatizar las peticiones. Monitoree el consumo de recursos de su máquina para documentar la VRAM adecuadamente. 

- MD 

### Fase 4: Experimentación y Vibe Coding (Componente 3) 

Esta fase evalúa el impacto de la IA en la escritura de código. 

Componente 3 - Comparación de modelos (20%): 

- El objetivo es resolver un mismo problema de programación propuesto por el docente utilizando tres enfoques distintos. 

MD 

- Los enfoques requeridos son: un modelo local generalista, un modelo local especializado en código y un modelo de desarrollo cloud (como Codex). 

- MD 

- El problema será pequeño y verificable, como por ejemplo consumir una API pública, validar la respuesta, calcular estadísticas y generar una visualización. 

- MD 

Se debe documentar una comparación que incluya: código ejecutable, errores encontrados, iteraciones necesarias, tiempo hasta la solución, claridad del código, pruebas sugeridas e intervención humana. 

MD 

Estrategia: Defina un prompt base muy estructurado para el problema. Ejecútelo en los tres modelos de forma aislada. Aproveche su experiencia configurando pruebas unitarias (como NUnit en otros lenguajes) para analizar objetivamente si el código Python entregado por los modelos aprueba la validación de datos requerida sin generar excepciones. Documente cada iteración y corrección necesaria hasta llegar a la solución. 

MD 

Comencemos por partes, primero por el componente 0 

Para estructurar el mapa mental del Componente 0, cada nodo debe conectarse lógicamente y responder de forma obligatoria a qué es, para qué sirve, un ejemplo práctico y su aplicación específica dentro del flujo de trabajo de este proyecto. A continuación, se detalla el contenido técnico estructurado para las cinco ramas requeridas. 

MD + 1 

### 1. Fundamentos 

Inteligencia Artificial (IA) y Machine Learning (ML): La IA es el campo amplio de creación de sistemas que emulan capacidades cognitivas, mientras que el ML es la disciplina donde 

los algoritmos aprenden patrones a partir de datos sin ser programados con reglas explícitas. Sirven como el marco teórico y práctico de la automatización avanzada. Ejemplo: Sistemas de detección de fraude. En el laboratorio: El ML proporciona la base matemática para la predicción de series temporales en el reto integrador. 

- MD 

Deep Learning y Redes Neuronales: Subconjunto del ML basado en múltiples capas de nodos interconectados (neuronas artificiales). Sirven para procesar representaciones de alta dimensionalidad. Ejemplo: Visión por computadora. En el laboratorio: Son el motor arquitectónico subyacente de todos los modelos a evaluar. 

- MD 

- Transformers y Modelos Fundacionales: Los Transformers son una arquitectura basada en mecanismos de atención que procesan secuencias completas en paralelo, permitiendo entrenar Modelos Fundacionales a escala masiva. Sirven para comprender contexto profundo y adaptarse a múltiples tareas. Ejemplo: GPT-4. En el laboratorio: Representan la arquitectura base de los modelos locales y en la nube que usted implementará. MD 

### 2. Tipos de Modelos 

- LLM, SLM y Modelos de Código: Los Grandes (LLM) y Pequeños (SLM) Modelos de Lenguaje generan texto basándose en probabilidades, con variantes altamente especializadas en sintaxis de programación. Sirven para documentar, refactorizar o generar lógica de software. Ejemplo: Llama 3 (LLM), Phi-3 (SLM), Qwen-Coder (Código). En el laboratorio: Serán los sujetos directos de comparación durante la práctica de Vibe Coding. 

- MD 

- VLM, Multimodales, Embeddings, STT y TTS: Los VLM procesan imágenes y texto combinados; los Embeddings convierten información en vectores numéricos para búsqueda semántica; STT y TTS transcriben audio a texto y viceversa. Sirven para interactuar con datos no estructurados. Ejemplo: LLaVA (VLM) o Whisper (STT). En el laboratorio: Deberán investigarse detalladamente para construir la cartografía del Componente 1. 

- MD 

### 3. Funcionamiento Interno 

- Parámetros, Entrenamiento e Inferencia: Los parámetros son los pesos matemáticos ajustados durante el entrenamiento (fase de aprendizaje costosa computacionalmente). La inferencia es el paso de datos nuevos por estos pesos para obtener una respuesta. Sirven para definir la capacidad cognitiva del modelo. Ejemplo: Un modelo optimizado de 8 mil millones de parámetros (8B). En el laboratorio: Toda la práctica se centrará exclusivamente en la ejecución de la etapa de inferencia. 

- MD 

- Tokens y Ventana de Contexto: Los tokens son las unidades mínimas de texto procesadas, y la ventana de contexto es el límite de tokens que el modelo retiene en memoria por petición. Sirven para limitar el tamaño de las entradas. Ejemplo: Ventana máxima de 8k tokens. En el laboratorio: Será el factor limitante al enviar estructuras de datos o scripts largos al modelo para su evaluación. 

- MD 

- Temperatura y Cuantización: La temperatura ajusta la aleatoriedad probabilística (creatividad), y la cuantización reduce la precisión numérica de los parámetros (ej. de 16 a 4 bits). Sirven para controlar la exactitud de la respuesta y comprimir el peso del modelo en disco. Ejemplo: Formato GGUF cuantizado. En el laboratorio: La cuantización será indispensable para que los modelos se ejecuten sin agotar la memoria de su máquina. MD 

### 4. Entornos de Ejecución e Infraestructura 

- Modelo Local vs. Cloud y Hardware (CPU, GPU, RAM, VRAM): La inferencia local procesa los datos en su propio hardware (dependiendo críticamente de la VRAM y la RAM), mientras que la nube delega el procesamiento a granjas de servidores. Sirven para gestionar el tradeoff entre privacidad de datos, costos y latencia. Ejemplo: Levantar un modelo en una GPU dedicada vs. consumir OpenAI. En el laboratorio: Requerirá registrar los consumos de recursos físicos locales frente a la velocidad de la alternativa cloud. 

MD 

API, Entornos (Ollama / LM Studio) y Licencias (Open-weight vs. Propietario): Ollama y LM Studio actúan como rígidamente contenedores o servidores que exponen los modelos (con pesos públicos u open-weight) a través de interfaces REST o de chat. Sirven para integrar las capacidades generativas en arquitecturas backend. Ejemplo: Hacer un POST HTTP a 

localhost:11434 . En el laboratorio: Usted orquestará esta infraestructura consumiendo un modelo desde un script programático en Python mediante una API local. MD 

Tengo entendido que para el componente 0 debo elaborar un mapa mental ¿no? 

Sí, el Componente 0 exige la elaboración de un mapa mental técnico que debe entregarse en PDF, PNG o mediante un enlace a la herramienta utilizada. Este entregable corresponde al 15 % de la evaluación del laboratorio. 

##### MD + 1 

El documento establece los siguientes lineamientos obligatorios para su construcción: 

- Propósito: No debe ser una lista de definiciones aisladas, sino que debe evidenciar relaciones, dependencias y ejemplos entre los diferentes conceptos. MD 

- Estructura de las respuestas: Cada concepto incluido debe responder de forma breve a cuatro puntos: ¿qué es?, ¿para qué sirve?, un ejemplo y dónde se utilizará durante el laboratorio. 

- MD 

Contenido mínimo requerido (Ramas): 

- Fundamentos: Inteligencia Artificial, Machine Learning, Deep Learning, redes neuronales, Transformers y modelos fundacionales. 

- MD 

- Tipos de modelos: LLM, SLM, VLM, modelos de código, modelos multimodales, embeddings, Speech-to-Text y Text-to-Speech. 

- MD 

- Funcionamiento: Parámetros, tokens, ventana de contexto, inferencia, temperatura, cuantización, y la diferencia entre entrenamiento vs. inferencia. 

- MD 

- Formas de uso: Modelo local, modelo cloud, API, interfaz de chat, open-weight y modelo propietario. MD 

- Infraestructura: CPU, GPU, RAM, VRAM, Ollama, LM Studio y servicios cloud. MD 

Estoy pidiendo que me ayudes a elaborar este mapa mental, dame el contenido (no te centres solo en lo mínimo, da un poco más) creería que puede ser en formato markdown, posterior me voy a una herramienta adicional que me permita elaborar el mapa mental 

Comprendo. Le presento una estructura detallada en formato Markdown que cumple con todas las exigencias del documento y expande un poco más los conceptos técnicos para que su mapa mental sea robusto. 

Esta estructura jerárquica está lista para ser copiada y pegada en herramientas de generación de mapas mentales a partir de Markdown (como Markmap, Obsidian, o incluso adaptada a esquemas PlantUML). 

Cada concepto responde estrictamente a las cuatro preguntas requeridas: ¿qué es?, ¿para qué sirve?, un ejemplo y dónde se utilizará en el laboratorio. 

MD 

<mark></mark> 

Markdown 

# Componente 0 - Mapa mental: Fundamentos de modelos de IA 

## 1. Fundamentos[cite: 1] 

- **Inteligencia Artificial (IA)**[cite: 1] 

- * *¿Qué es?:* Campo de la informática enfocado en crear sistemas capaces de emular fu * *¿Para qué sirve?:* Para automatizar tareas complejas, resolver problemas lógicos y * *Ejemplo:* Un sistema de recomendación o un agente virtual. * *Uso en el lab:* Es el marco teórico general bajo el cual se desarrollará todo el cic 

- * **Machine Learning (ML)**[cite: 1] * *¿Qué es?:* Subdisciplina de la IA donde los sistemas aprenden patrones a partir de * *¿Para qué sirve?:* Para predicciones, clasificaciones y análisis de tendencias. * *Ejemplo:* Un algoritmo de regresión lineal para predecir precios. * *Uso en el lab:* Constituye la base matemática y conceptual para la predicción de ser 

- * **Deep Learning**[cite: 1] * *¿Qué es?:* Rama del ML basada en redes neuronales artificiales con múltiples capas * *¿Para qué sirve?:* Para procesar datos de alta dimensionalidad y no estructurados ( * *Ejemplo:* Reconocimiento facial avanzado. * *Uso en el lab:* Es la tecnología subyacente que permite el funcionamiento de todos l 

- * **Redes Neuronales**[cite: 1] * *¿Qué es?:* Arquitecturas de software inspiradas en el cerebro biológico, compuesta * *¿Para qué sirve?:* Para aproximar funciones complejas y transmitir información a tr * *Ejemplo:* Red Neuronal Convolucional (CNN) para visión. * *Uso en el lab:* Fundamento de la arquitectura interna de los LLMs. 

- * **Transformers**[cite: 1] * *¿Qué es?:* Arquitectura de red neuronal introducida en 2017 basada en "mecanismos * *¿Para qué sirve?:* Para capturar el contexto a largo plazo en secuencias de datos ( * *Ejemplo:* La arquitectura "T" en GPT (Generative Pre-trained Transformer). * *Uso en el lab:* Arquitectura base de los modelos de Vibe Coding[cite: 1]. 

- * **Modelos fundacionales**[cite: 1] * *¿Qué es?:* Modelos de IA masivos, entrenados con grandes cantidades de datos no et * *¿Para qué sirve?:* Como modelo base (foundation) sobre el cual se construyen soluci * *Ejemplo:* Llama 3 o GPT-4. * *Uso en el lab:* Serán los motores principales consultados tanto en el entorno local 

- ## 2. Tipos de modelos[cite: 1] * **LLM (Large Language Model)**[cite: 1] * *¿Qué es?:* Modelo fundacional especializado en comprender y generar lenguaje natur * *¿Para qué sirve?:* Para redacción, resumen, traducción y razonamiento lógico genera * *Ejemplo:* Mixtral 8x7B. * *Uso en el lab:* Será el "modelo local generalista" utilizado en la comparación de có 

- * **SLM (Small Language Model)**[cite: 1] * *¿Qué es?:* Versión reducida y optimizada de un LLM, con menos parámetros. * *¿Para qué sirve?:* Para ejecutar tareas de lenguaje en hardware con recursos limita * *Ejemplo:* Phi-3 Mini. * *Uso en el lab:* Alternativa ideal para la ejecución local si el hardware disponible 

- * **Modelos de código**[cite: 1] * *¿Qué es?:* Modelos entrenados específicamente sobre vastos repositorios de código * *¿Para qué sirve?:* Para autocompletar código, generar scripts en Python, C#, TypeSc * *Ejemplo:* Qwen-Coder o StarCoder. * *Uso en el lab:* Herramienta central para la práctica de Vibe Coding y el reto integr 

- * **VLM (Vision-Language Model) y Multimodales**[cite: 1] * *¿Qué es?:* Modelos capaces de procesar y relacionar múltiples tipos de datos simul * *¿Para qué sirve?:* Para analizar diagramas de arquitectura, describir imágenes o ge * *Ejemplo:* LLaVA. * *Uso en el lab:* Parte de la investigación en la cartografía de modelos del ecosistem 

- * **Embeddings**[cite: 1] * *¿Qué es?:* Representaciones vectoriales (matrices de números) de palabras o fragme * *¿Para qué sirve?:* Para medir la similitud semántica entre textos y habilitar motor * *Ejemplo:* text-embedding-3-small. * *Uso en el lab:* Concepto clave a investigar en la cartografía[cite: 1], útil para bú 

- * **STT (Speech-to-Text) y TTS (Text-to-Speech)**[cite: 1] * *¿Qué es?:* Modelos de transcripción de voz a texto y síntesis de texto a voz gener * *¿Para qué sirve?:* Para interfaces conversacionales audibles y accesibilidad. * *Ejemplo:* Whisper (STT) y ElevenLabs (TTS). * *Uso en el lab:* Categoría obligatoria a investigar en la matriz cartográfica[cite: 1 

## 3. Funcionamiento[cite: 1] 

- **Entrenamiento vs. Inferencia**[cite: 1] 

* *¿Qué es?:* El entrenamiento es la creación del modelo ajustando pesos; la inferenc * *¿Para qué sirve?:* Diferenciar las fases del ciclo de vida de la IA. * *Ejemplo:* OpenAI entrena el modelo por meses; el usuario hace inferencia en segund * *Uso en el lab:* Todas las ejecuciones locales y por API del laboratorio serán exclus * **Parámetros y Cuantización**[cite: 1] 

* *¿Qué es?:* Los parámetros son las variables internas del modelo; la cuantización e 

- *¿Para qué sirve?:* Para reducir el tamaño del modelo en disco y el consumo de memor 

- * *Ejemplo:* Un modelo GGUF cuantizado a 4 bits (Q4). * *Uso en el lab:* Obligatorio aplicarlo al usar Ollama/LM Studio para evitar desbordam 

- * **Tokens y Ventana de contexto**[cite: 1] * *¿Qué es?:* Los tokens son fragmentos de palabras; la ventana de contexto es la can * *¿Para qué sirve?:* Para definir el límite de información de entrada (archivos, códi * *Ejemplo:* Ventana de contexto de 8k o 128k tokens. * *Uso en el lab:* Determinará qué tan largo puede ser el script de Python que le envíe 

- * **Temperatura**[cite: 1] * *¿Qué es?:* Un hiperparámetro de inferencia que controla la aleatoriedad de las pre * *¿Para qué sirve?:* Para hacer respuestas más deterministas y exactas (temperatura b * *Ejemplo:* Temperatura 0.1 para algoritmos, 0.8 para redacción. * *Uso en el lab:* Deberá ajustarse (idealmente cercana a 0) al solicitar soluciones de 

- * **System Prompt (Concepto Extra)** * *¿Qué es?:* La instrucción base o directiva global que configura el comportamiento * *¿Para qué sirve?:* Para fijar el rol, el tono y las restricciones del agente de IA * *Ejemplo:* "Eres un desarrollador experto en Python, responde solo con código ejecu * *Uso en el lab:* Esencial para estandarizar las respuestas durante la comparación de 

- ## 4. Formas de uso[cite: 1] * **Modelo local vs. Modelo cloud**[cite: 1] * *¿Qué es?:* Local se ejecuta en el hardware del usuario; Cloud se procesa en servid * *¿Para qué sirve?:* Local garantiza privacidad total de los datos y cero latencia de * *Ejemplo:* Correr Llama 3 en su máquina vs. consumir la API de OpenAI. * *Uso en el lab:* Deberá comparar ambos enfoques en la práctica de Vibe Coding evaluan 

- * **API (Application Programming Interface)**[cite: 1] * *¿Qué es?:* Interfaz que permite la comunicación programática entre dos sistemas de * *¿Para qué sirve?:* Para integrar las respuestas del modelo directamente en el backe * *Ejemplo:* Petición POST a un endpoint que devuelve un JSON. * *Uso en el lab:* Será necesario consumir un modelo local desde un programa Python med 

- * **Open-weight vs. Modelo propietario**[cite: 1] * *¿Qué es?:* Open-weight expone los pesos del modelo públicamente para uso libre; Pr * *¿Para qué sirve?:* Open-weight permite despliegues locales (Ollama); Propietario su * *Ejemplo:* Mistral (Open-weight) vs. Claude 3 (Propietario). * *Uso en el lab:* Instalará modelos open-weight en LM Studio/Ollama para las pruebas l 

- ## 5. Infraestructura[cite: 1] * **Hardware (CPU, GPU, RAM, VRAM)**[cite: 1] * *¿Qué es?:* Componentes físicos del equipo. CPU (Procesador central), GPU (Tarjeta * *¿Para qué sirve?:* Dictan la velocidad de inferencia (GPU) y el tamaño máximo del m * *Ejemplo:* Tarjeta gráfica con 8GB de VRAM. * *Uso en el lab:* Deberá registrar la observación de consumos de RAM/VRAM en su equipo 

- * **Ollama y LM Studio**[cite: 1] * *¿Qué es?:* Herramientas y runtimes diseñados para descargar, servir y ejecutar mod * *¿Para qué sirve?:* Ollama facilita levantar servidores de IA desde consola, mientra * *Ejemplo:* Ejecutar `ollama run llama3`. * *Uso en el lab:* Herramientas centrales requeridas para la ejecución local, la exposi 

- * **Servicios Cloud**[cite: 1] * *¿Qué es?:* Infraestructura proporcionada por terceros (AWS, Azure, GCP) o platafor * *¿Para qué sirve?:* Para escalar aplicaciones de IA sin gestionar clústeres físicos * *Ejemplo:* Azure OpenAI Service o un contenedor Docker en AWS consumiendo una API. * *Uso en el lab:* Será la base del modelo "Cloud coding" (como Codex o equivalente) qu 

Esta estructura mantiene el foco metodológico que se le exige. Puede llevar este código directamente a una herramienta como Markmap (visualmente muy limpia para Markdown) y generar su PDF o PNG final[cite: 1]. 



El error de sintaxis que observa en la imagen ocurre porque pegó el formato Markdown estándar directamente en el editor, y PlantUML requiere etiquetas y símbolos específicos para compilar un mapa mental. 

Para que PlantUML reconozca la estructura, debe envolver el documento entre las directivas @startmindmap y @endmindmap , y utilizar asteriscos ( * , ** , *** ) para definir la jerarquía de los nodos, eliminando los numerales ( # ) de Markdown. 

A continuación, le entrego el código exacto con la sintaxis de PlantUML lista para que la copie, pegue y genere su diagrama equilibrado (utilizando el comando left side para distribuir los nodos a ambos lados). 

|Fragmento de código<br>|
|---|
|@ttid|
|sarmnmap<br>* **Fundamentos de Modelos de IA**|
|** 1. Fundamentos<br>*** Inteligencia Artificial (IA)<br>|
|**** **¿Qué es?:** Sistemas que emulan funciones cognitivas.<br>**** **¿Para ué sirve?:** Automatizar tareas comlejas|
|q    p.<br>**** **Ejemplo:** Agente virtual.|
|**** **Uso en lab:** Marco teórico general.<br>|
|*** Machine Learning (ML)|
|**** **¿Qué es?:** Sistemas que aprenden patrones a partir de datos.<br>**** **¿Para qué sirve?:** Predicciones y análisis de tendencias.|
|**** **Ejemplo:** Regresión lineal.<br>|
|**** **Uso en lab:** Base matemática para series temporales.<br>|
|*** Deep Learning<br>**** **é **    úi|
|¿Qu es?: Redes neuronales con mltples capas.<br>**** **¿Para qué sirve?:** Procesar datos de alta dimensionalidad.<br>ii i|
|**** **Ejemplo:** Reconocmento facal.|
|**** **Uso en lab:** Tecnología subyacente de los modelos generativos.<br>|
|*** Redes Neuronales|
|**** **¿Qué es?:** Nodos interconectados inspirados en el cerebro.|
|**** **¿Para qué sirve?:** Aproximar funciones complejas.<br>|
|**** **Ejemplo:** Red Neuronal Convolucional (CNN).|
|**** **Uso en lab:** Fundamento de la arquitectura interna.<br>|
|*** Transformers<br>**** **¿Qué es?:** Aruitectura basada en "mecanismos de atención"|
|q     .<br>**** **¿Para qué sirve?:** Capturar contexto a largo plazo en secuencias.|
|**** **Ejemplo:** Arquitectura GPT.<br>|
|**** **Uso en lab:** Arquitectura base de los modelos evaluados.<br>*** Modelos fundacionales<br>|
|**** **¿Qué es?:** Modelos masivos adaptables a múltiples tareas.|
|**** **¿Para qué sirve?:** Base para soluciones específicas.<br>|
|**** **Ejemplo:** Llama 3 o GPT-4.<br>**** **Uso en lab:** Motores principales a consultar.|
|** 2. Tipos de modelos<br>*** LLM (Large Language Model)|
|**** **¿Qué es?:** Especializado en lenguaje natural.<br>|
|**** **¿Para qué sirve?:** Redacción y razonamiento lógico.<br>**** **Ejemplo:** Mixtral 8x7B.|
|<br>**** **Uso en lab:** Modelo local generalista.<br>|
|*** SLM (Small Language Model)<br>**** **é ?** Vió did d  LLM|
|¿Qu es: ersn reuca e un .<br>|
|**** **¿Para qué sirve?:** Tareas en hardware limitado.<br>**** **** i ii|
|Ejemplo: Ph-3 Mn.|
|**** **Uso en lab:** Alternativa para equipos con poca RAM.<br>|
|*** Modelos de código<br>|
|**** **¿Qué es?:** Entrenados sobre repositorios de código.<br>**** **¿Para qué sirve?:** Generar y explicar lógica de software.<br>|
|**** **Ejemplo:** Qwen-Coder.|
|**** **Uso en lab:** Herramienta central para Vibe Coding.<br>|
|*** VLM y Multimodales<br>**** **¿Qué es?:** Procesan texto imagen o video simultáneamente|
|,    .<br>**** **¿Para qué sirve?:** Analizar diagramas o interfaces visuales.|
|**** **Ejemplo:** LLaVA.<br>|
|**** **Uso en lab:** Investigación en la cartografía.|
|*** Embeddings<br>|
|**** **¿Qué es?:** Representaciones vectoriales de datos.|
|**** **¿Para qué sirve?:** Búsqueda semántica.<br>|
|**** **Ejemplo:** text-embedding-3-small.|
|**** **Uso en lab:** Investigación cartográfica.<br>***|
|STT y TTS|
|**** **¿Qué es?:** Transcripción de voz y síntesis de texto.<br>**** **P é i?** If dibl|
|¿ara qu srve: nteraces aues.<br>**** **Ejemplo:** Whisper (STT).|



**** **Uso en lab:** Categoría a investigar. left side ** 3. Funcionamiento *** Entrenamiento vs. Inferencia **** **¿Qué es?:** Crear el modelo vs. usar el modelo. **** **¿Para qué sirve?:** Diferenciar fases del ciclo de IA. **** **Ejemplo:** OpenAI entrena, el usuario hace inferencia. **** **Uso en lab:** Todas las ejecuciones serán inferencia. *** Parámetros y Cuantización **** **¿Qué es?:** Variables del modelo y su compresión (ej. 4-bit). **** **¿Para qué sirve?:** Reducir consumo de memoria. **** **Ejemplo:** Modelo GGUF Q4. **** **Uso en lab:** Evitar desbordamientos de RAM/VRAM. *** Tokens y Ventana de contexto **** **¿Qué es?:** Fragmentos de texto y límite de memoria a corto plazo. **** **¿Para qué sirve?:** Definir límite de entrada de datos. **** **Ejemplo:** Ventana de 8k tokens. **** **Uso en lab:** Limitará el tamaño de los scripts enviados. *** Temperatura **** **¿Qué es?:** Hiperparámetro de aleatoriedad. **** **¿Para qué sirve?:** Controlar exactitud vs. creatividad. **** **Ejemplo:** Temperatura 0.1 para código. **** **Uso en lab:** Ajustar para obtener código ejecutable. ** 4. Formas de uso *** Modelo local vs. Cloud **** **¿Qué es?:** Hardware propio vs. servidores externos. **** **¿Para qué sirve?:** Balancear privacidad y potencia. **** **Ejemplo:** Llama 3 local vs. API de OpenAI. **** **Uso en lab:** Comparar ambos enfoques en Vibe Coding. *** API **** **¿Qué es?:** Interfaz de comunicación programática. **** **¿Para qué sirve?:** Integrar IA en backends. **** **Ejemplo:** Petición POST a un endpoint. **** **Uso en lab:** Consumo de modelos locales y series temporales. *** Open-weight vs. Propietario **** **¿Qué es?:** Pesos públicos vs. caja negra controlada. **** **¿Para qué sirve?:** Despliegues locales vs. servicios gestionados. **** **Ejemplo:** Mistral vs. Claude 3. **** **Uso en lab:** Instalar modelos open-weight en Ollama. ** 5. Infraestructura *** Hardware (CPU, GPU, RAM, VRAM) **** **¿Qué es?:** Componentes de procesamiento y memoria. **** **¿Para qué sirve?:** Dictan velocidad y tamaño máximo del modelo. **** **Ejemplo:** GPU con 8GB de VRAM. **** **Uso en lab:** Registrar consumo de recursos en las pruebas. *** Ollama y LM Studio **** **¿Qué es?:** Runtimes para servir modelos locales. **** **¿Para qué sirve?:** Levantar servidores IA fácilmente. **** **Ejemplo:** Comando ollama run. **** **Uso en lab:** Herramientas de ejecución local. *** Servicios Cloud **** **¿Qué es?:** Infraestructura gestionada por terceros. **** **¿Para qué sirve?:** Escalar sin hardware propio. **** **Ejemplo:** Azure OpenAI. **** **Uso en lab:** Base del modelo cloud evaluado. @endmindmap 

Ahora, pasemos al componente 1 

El Componente 1 (Cartografía del ecosistema de modelos de IA - 20 %) exige construir una matriz comparativa con fuentes técnicas verificables y responder a la pregunta central de selección de modelos según restricciones reales (privacidad, hardware, costo, tarea). 

MD 

A continuación tiene la matriz técnica estructurada para las seis categorías obligatorias, junto con la resolución argumentada de la pregunta central. MD 

Matriz Comparativa del Ecosistema de Modelos 

|Modelo<br>Llama 3.1 8B Instruct|Proveedor<br>Meta AI|Tipo<br>Texto / Generalista|Local / Cloud<br>Local / Ambos|
|---|---|---|---|
|DeepSeek-R1 (o 14B<br>QwQ)|DeepSeek / Qwen|Razonamiento|Ambos (Pesos<br>y API)|
|Qwen2.5-Coder 7B (o<br>32B)|Alibaba Cloud (Qwen)|Desarrollo de software|Local / Ambos|
|Claude 3.5 Sonnet|Anthropic|Visión / Multimodal /<br>Código|Cloud|
|Whisper (Large-v3 /<br>Medium)|OpenAI|Voz (STT - Speech-to-<br>Text)|Local / Ambos|
|ElevenLabs<br>(Multilingual v2)|ElevenLabs|Voz (TTS - Text-to-<br>Speech)|Cloud|
|text-embedding-3-<br>small|OpenAI|Embeddings|Cloud|



|Resolución<br>¿Qué m<br>MD<br>No existe un<br>estricto entr<br>MD<br>Modelo<br>bge-m3<br><br>Privaci<br>1.<br>|de la Pregunta Central<br>odelo utilizaría para cada tipo de problema y por qué?<br>modelo universal óptimo. La selección técnica debe responder a un balance<br>e cuatro restricciones:<br>Proveedor<br>Tipo<br>Local / Cloud<br>BAAI<br>Embeddings<br>Local / Ambos<br>dad y cumplimiento normativo:<br>|
|---|---|
|1.|Si la tarea procesa datos sensibles, credenciales, código fuente propietario o|
||información médica/financiera regulada la decisión se inclina haciamodelos|
||,<br>locales open-weightcomoQwen2.5-CoderoLlama 3.1 8B. Aunque sacrifican un|
|Capac<br>2.<br>1.|margen menor de precisión frente a modelos de cientos de miles de millones de<br>parámetros, garantizan que los datos jamás abandonen el perímetro de la red<br>local.<br>idad de cómputo y hardware disponible:<br>En estaciones de trabajo con GPUs estándar (6-8 GB VRAM), modelos compactos|
||<br>comoQwen2.5-Coder 7Bo versionesSLMcuantizadas a 4 bits (<br>Q4_K_M ) son<br>viables para desarrollo interactivo.|
|2.|Si el hardware carece de aceleración gráfica dedicada o la memoria RAM es|
||limitada, forzar modelos de razonamiento masivo de forma local genera tiempos|
||<br>de inferencia inaceptables; en ese escenario, delegar la carga aAPIs gestionadas|
||en la nube(como Claude o la API de DeepSeek) es la única vía viable para<br>mantener la productividad.|
|Costo<br>3.|operativo frente a volumen:|
|1.|Para flujos de alta concurrencia o procesamiento continuo (como embeber miles|
||<br>de registros por minuto para un motor de búsqueda), un modelo de embeddings|
||local (bge-m3) elimina costos recurrentes por llamadas a API.|
|2.|En contraste, para tareas esporádicas pero de alta complejidad analítica (como la|
||conceptualización inicial de un módulo de software o refactorizaciones<br>|
||profundas), el pago por token deClaude 3.5 Sonnetse amortiza directamente<br>con la reducción en horas de depuración humana.|
|Natura<br>4.<br>|leza de la tarea:<br>|
|1.|Programación iterativa:Modelos especializados en sintaxis (Qwen2.5-Coder /|
||Claude 35 Sonnet) superan ampliamente a los generalistas ya que comprenden|
||.      ,<br>convenciones de frameworks, tipado estricto y pruebas unitarias con menor tasa<br>de alucinación sintáctica.|
|2.|Deducción lógica pura:Modelos con capacidad de razonamiento explícito<br>(reasoning models) son necesarios para resolver algoritmos no convencionales o<br>análisis de consistencia matemática.|
|Fuentes Té|cnicas Oficiales de Verificación|
|Meta AI<br>(https:|:Documentación técnica y model cards de Llama 3.1 (<br>[ai.meta.com/llama]<br>//ai.meta.com/llama) ).|



Qwen Team (Alibaba): Repositorio y métricas de Qwen2.5-Coder en Hugging Face ( huggingface.co/Qwen ). 

DeepSeek: Reporte técnico de DeepSeek-R1 y documentación de API ( apidocs.deepseek.com ). 

Anthropic: Especificaciones y system cards de Claude 3.5 ( docs.anthropic.com ). 

OpenAI: Guías de modelos Whisper y Embeddings v3 ( [platform.openai.com/docs/models] 

(https://platform.openai.com/docs/models) ). 

BAAI (Beijing Academy of Artificial Intelligence): Documentación técnica de BGE-M3 ( huggingface.co/BAAI/bge-m3 ). 



<!-- Start of picture text -->
Ahora, el componente 2<br><!-- End of picture text -->

El Componente 2 (Laboratorio de modelos locales: Ollama + LM Studio - 20 %) se enfoca en la ejecución local, el monitoreo del hardware y la integración programática mediante una API local. MD 

A continuación se detalla la guía paso a paso, la explicación del flujo arquitectónico exigido, los scripts en Python listos para su repositorio y la plantilla para el registro técnico. 

MD 

### 1. Relación Arquitectónica Fundamental 

El laboratorio exige explicar la siguiente cadena de integración: 

MD 

Plaintext 

<mark></mark> 

MODELO -> OLLAMA / LM STUDIO -> API LOCAL -> APLICACIÓN PYTHON 

   - Modelo: Son los pesos matemáticos ( .gguf ) entrenados para generar secuencias probabilísticas de texto o código. 

   - Ollama / LM Studio (Runtime & Servidor): Actúan como el motor de ejecución e inferencia sobre el hardware (CPU/GPU/VRAM) y levantan un servidor HTTP local que expone puertos de red ( 11434 en Ollama, 1234 en LM Studio). 

   - API Local: Es la interfaz REST estandarizada que recibe peticiones HTTP con payloads JSON (siguiendo especificaciones tipo OpenAI o nativas) y devuelve respuestas estructuradas. 

   - Aplicación Python (Cliente): Es el código consumidor que prepara el prompt, envía la solicitud HTTP a la API local, deserializa el JSON de respuesta y procesa el resultado para el usuario final. 

2. Configuración y Ejecución de Modelos Entorno A: Ollama 

1. Descargue e instale Ollama en su sistema operativo. 

2. Desde la terminal, descargue un modelo generalista y un modelo orientado a desarrollo de software: MD Bash <mark></mark> # Modelo generalista (Llama 3.1 8B cuantizado) ollama pull llama3.1 

<mark></mark> 

# Modelo especializado en código ollama pull qwen2.5-coder:7b 

3. El servicio de Ollama quedará activo en segundo plano en http://localhost:11434 . 

### Entorno B: LM Studio 

1. Instale LM Studio y abra la interfaz gráfica. 

2. En la pestaña de búsqueda (Search), busque y descargue un modelo cuantizado compatible (por ejemplo, qwen2.5-coder-7b-instruct o mistral-7b-instruct en cuantización Q4_K_M ). 

3. Vaya a la pestaña del servidor local (Local Server / Desarrollador), seleccione el modelo descargado y haga clic en Start Server. Por defecto, expondrá una API compatible con OpenAI en http://localhost:1234/v1 . 

### 3. Código Fuente Consumidor (Python) 

Siguiendo la estructura del repositorio ( /modelos_locales/ollama_test.py y lmstudio_test.py ), utilice la librería nativa requests para consumir directamente las APIs REST locales sin dependencias innecesarias. 

MD + 1 

### modelos_locales/ollama_test.py 

> Python <mark></mark> import json import time import requests def test_ollama(): url = "http://localhost:11434/api/generate" model_name = "qwen2.5-coder:7b" prompt = "Escribe una función en Python para calcular la media móvil de una lista de f payload = { "model": model_name, "prompt": prompt, "stream": False, "options": { "temperature": 0.2 } } print(f"Enviando solicitud a Ollama (Modelo: {model_name})...") start_time = time.time() try: response = requests.post(url, json=payload) response.raise_for_status() data = response.json() elapsed_time = time.time() - start_time print(f"Respuesta recibida en {elapsed_time:.2f} segundos.\n") print("--- RESPUESTA GENERADA ---") print(data.get("response", "")) print("---------------------------") except requests.exceptions.ConnectionError: print("Error: No se pudo conectar a Ollama. Verifique que el servicio esté corrien if __name__ == "__main__": test_ollama() 

### modelos_locales/lmstudio_test.py 

> Python  import time import requests def test_lmstudio(): # LM Studio expone un endpoint compatible con el estándar OpenAI v1/chat/completions url = "http://localhost:1234/v1/chat/completions" payload = { "messages": [ {"role": "system", "content": "Eres un asistente de software enfocado en escri {"role": "user", "content": "Escribe una función en Python para calcular la me ], "temperature": 0.2, "max_tokens": 512 } print("Enviando solicitud a LM Studio (API Local: 1234)...") start_time = time.time() try: response = requests.post(url, json=payload) response.raise_for_status() data = response.json() elapsed_time = time.time() - start_time answer = data["choices"][0]["message"]["content"] print(f"Respuesta recibida en {elapsed_time:.2f} segundos.\n") print("--- RESPUESTA GENERADA ---") print(answer) print("---------------------------") except requests.exceptions.ConnectionError: print("Error: No se pudo conectar a LM Studio. Verifique que el servidor local est if __name__ == "__main__": test_lmstudio() 

### 4. Plantilla de Registro de Recursos y Evidencias 

Para cumplir con el requerimiento de evidencia observable de hardware y tiempos, agregue este registro técnico dentro del repositorio (por ejemplo en 

modelos_locales/registro_tecnico.md ): 

MD 

|Entorno / Runtime|Modelo Evaluado|Cuantización|Memoria Observ<br>(RAM / VRAM)|
|---|---|---|---|
|Ollama|llama3.1:8b<br>(Generalista)<br>MD|Q4_K_M|~5.2 GB VRAM / ~2<br>RAM|
|Ollama|qwen2.5-coder:7b<br>(Código)|Q4_K_M|~4.9 GB VRAM / ~1<br>RAM|
||MD|||
|LM Studio|qwen2.5-coder-7b-<br>instruct<br>MD|Q4_K_M|~5.1 GB VRAM / ~2<br>RAM|



Evidencias para la entrega: Guarde en la carpeta /evidence capturas de pantalla de la terminal con Ollama corriendo, de la interfaz de LM Studio con el servidor activo y de la ejecución de ambos scripts de Python mostrando los resultados por consola. 

MD 

MD 



Como contexto, ya tengo instalados LM STUDIO y OLLAMA 

Teniendo ya instalados y operativos Ollama y LM Studio en su sistema, el Componente 2 queda prácticamente cubierto a nivel de entorno y podemos estructurar directamente el Componente 3: Práctica de Vibe Coding (Comparación de modelos - 20 %). 

##### MD 

Este componente evalúa cómo varía el ciclo de desarrollo asistido al enfrentar un mismo problema de programación contra tres categorías de modelos: 

##### MD 

1. Modelo local generalista: por ejemplo, llama3.1:8b ejecutado en Ollama. 

   - MD 

2. Modelo local especializado en código: por ejemplo, qwen2.5-coder:7b ejecutado en Ollama o LM Studio. 

   - MD 

3. Modelo de desarrollo en la nube: por ejemplo, Claude 3.5 Sonnet, GitHub Copilot o GPT4o. 

   - MD 

A continuación se detalla la propuesta del problema, el prompt estandarizado, el flujo iterativo y la matriz comparativa que debe documentar en vibe_coding/comparativo.md . 

MD 

### 1. Definición del Problema de Prueba 

Para cumplir con el criterio de un reto pequeño, medible y verificable, utilizaremos la API pública y sin autenticación de Open-Meteo: 

##### MD 

Enunciado: Construir un script en Python que consulte las temperaturas horarias de los últimos 7 días para unas coordenadas dadas, valide que la estructura JSON contenga los campos requeridos, calcule la temperatura media, máxima y mínima, y genere un gráfico de línea guardado como temperatura.png . 

### 2. Prompt Estandarizado de Prueba 

Para garantizar una comparación metodológicamente válida, envíe exactamente el mismo prompt a los tres modelos sin modificaciones iniciales: 

#### Plaintext 

<mark></mark> 

Escribe un script en Python que realice lo siguiente: 

1. Consuma la API pública de Open-Meteo para obtener las temperaturas de los últimos 7 día URL: https://api.open-meteo.com/v1/forecast?latitude=5.0689&longitude=-75.5174&past_day 

2. Valide que la respuesta HTTP sea 200 y que el JSON contenga las llaves 'hourly' -> 'tim 

3. Cargue los datos en un DataFrame de Pandas, convierta las fechas a formato datetime y v 

4. Calcule e imprima por consola: media, mediana, valor mínimo y valor máximo. 

5. Genere y guarde una gráfica de línea de la temperatura a lo largo del tiempo en un arch Usa tipado estático, manejo explícito de excepciones y añade comentarios concisos. 

3. Ciclo de Trabajo Documentado (Vibe Coding) 

El documento exige registrar el ciclo iterativo de desarrollo: 

MD 

#### Plaintext 

<mark></mark> 

PROBLEMA -> PROMPT -> MODELO -> CÓDIGO -> EJECUCIÓN -> ERROR/RESULTADO -> CORRECCIÓN -> SO 

Para cada modelo, registre en su bitácora: 

- Entrada inicial: El prompt base. 

- Primera respuesta: Si el código corrió a la primera (zero-shot) o si arrojó errores de sintaxis, dependencias faltantes o accesos incorrectos al JSON. 

- Iteración correctiva: Qué prompt de ajuste tuvo que suministrarle (por ejemplo: "Corrige el error KeyError: 'temperature_2m' en la línea 24"). 

- Intervención humana: Las modificaciones manuales que usted como ingeniero debió realizar para que el script funcionara correctamente. 

- MD 

### 4. Matriz Comparativa para vibe_coding/comparativo.md 

Diligencie esta tabla en su informe con los datos reales observados durante sus ejecuciones: 

##### MD 

|Criterio de Evaluación<br>MD|Local Generalista<br>(<br>llama3.1:8b )<br>MD|Local Especializado<br>(<br>qwen2.5-coder:7b )<br>MD|Cloud Coding (C<br>/ GPT-4o)<br>MD|
|---|---|---|---|
|Código ejecutable al<br>primer intento<br>MD|Parcial (suele omitir<br>imports o fallar en el<br>indexado del JSON)|Alto (código funcional<br>con sintaxis moderna de<br>Pandas)|Total (genera códi<br>modular, robusto<br>errores sintáctico|
|Errores encontrados<br>MD|Nombres de columnas<br>incorrectos o mal manejo<br>de excepciones HTTP|Detalles menores de<br>formato de fecha o estilo<br>de gráfica|Prácticamente nu<br>tareas estándar de<br>scripting|
|Iteraciones necesarias<br>MD|2 a 3 prompts de<br>corrección|1 iteración de ajuste fino|0 a 1 iteración|
|Tiempo hasta la solución<br>funcional|~4 - 6 minutos (incluye<br>depuración)|~2 - 3 minutos|< 1 minuto|
|MD<br>Calidad y claridad del<br>código<br>MD|Aceptable, pero con<br>mezclas de estilos o<br>tipado incompleto|Alta, respeta PEP 8 y<br>tipado estático<br>(<br>typing )|Excelente, incluye<br>docstrings detalla<br>separación de fun|
|Documentación y<br>comentarios<br>MD|Explicaciones<br>excesivamente<br>conversacionales fuera<br>del código|Comentarios técnicos<br>directos en el código<br>fuente|Explicación estruc<br>del bloque de cód<br>cómo ejecutarlo|
|Pruebas sugeridas /<br>generadas<br>MD|Solo sugiere imprimir<br>variables por consola|Propone aserciones<br>básicas o bloques<br>try/except|Genera suite de p<br>con<br>pytesto d<br>simulados (mocks|
|Intervención humana<br>requerida<br>MD|Media/Alta (requiere<br>depurar lógica de<br>parsing)|Baja (supervisión de<br>dependencias y<br>ejecución)|Mínima (solo revis<br>validación de ejec|



### 5. Guía para la Reflexión Técnica Conclusiva 

El entregable solicita una reflexión técnica breve sobre qué cambió al utilizar modelos diferentes . Enfoque su análisis en estos tres ejes: 

##### MD 

1. Especialización vs. Tamaño: Un modelo local de código pequeño (7B-8B) supera a modelos generalistas de similar tamaño en estructuración sintáctica, nombres idiomáticos de variables y comprensión de APIs de librerías como Pandas o Requests. 

2. Latencia y Privacidad: El modelo local responde sin dependencia de conexión externa ni costos por token, pero exige capacidad de hardware en la máquina y produce soluciones más lineales. 

3. El rol del desarrollador en el "Vibe Coding": La IA reduce el tiempo de escritura mecánica (boilerplate), pero la responsabilidad crítica del ingeniero permanece en la verificación de tipos, la validación del esquema de datos entrante y la comprobación de que los cálculos estadísticos sean matemáticamente correctos. 

   - MD 

¿Desea que definamos el script de solución base para que pueda compararlo contra lo que generen sus modelos locales en Ollama y LM Studio? 



Antes de pasar al componente3... 

Así estoy guardando cada entregable, en el contexto del componente2 ¿Cómo recomiendas mejor la estructura y qué 

Para mantener la coherencia con la organización que ya ha establecido (carpetas Componente0 y Componente1 ) y cumplir con la estructura de repositorio sugerida en la sección 10 del documento base, le sugiero crear una carpeta llamada Componente2 (o 

Componente2_Modelos_Locales ). 

##### PNG + 1 

Dentro de ese directorio, debe alojar los scripts consumidores y las evidencias técnicas de ejecución. 

##### MD 

Estructura de archivos recomendada para el Componente 2: 

- Plaintext <mark></mark> 📁 Componente2 ├── 📄 ollama_test.py ├── 📄 lmstudio_test.py ├── 📄 registro_tecnico.md └── 📁 evidencias ├── 🖼 terminal_ollama.png └── 🖼 interfaz_lmstudio.png 

Propósito de cada elemento: 

ollama_test.py : El script en Python que realiza la petición HTTP a la API local de Ollama para probar el modelo generalista y el de código. MD 

lmstudio_test.py : El script en Python configurado para consumir el servidor local de LM Studio mediante su endpoint compatible con OpenAI. 

- MD 

- registro_tecnico.md : El archivo donde usted documentará formalmente la tabla 

- comparativa exigida: nombre del modelo, cuantización utilizada, consumo observado de RAM/VRAM y tiempo de inferencia. 

- MD 

Carpeta evidencias/ : Un subdirectorio destinado a almacenar las capturas de pantalla que demuestren la instalación operativa de Ollama, el servidor activo en LM Studio y el resultado impreso en consola por sus scripts de Python. 

MD 

Esta separación modular le permitirá migrar fácilmente los archivos a la estructura final del repositorio Git ( /modelos_locales y /evidence ) cuando deba empaquetar el proyecto completo para su entrega. 

MD 

cómo pruebo los archivos .py? cómo verifico que los modelos quedaron instalados? para adjuntar evidencias 

A continuación, se detalla el procedimiento técnico para verificar la disponibilidad de los modelos, ejecutar los scripts y recolectar las capturas exigidas para la carpeta de evidencias. 

MD 

### 1. Verificación de modelos instalados (Generación de evidencias) 

1. Ollama: Abra su terminal (PowerShell, CMD o la terminal de su IDE) y ejecute el siguiente comando: 

Bash 

<mark></mark> 

ollama list 

Este comando listará todos los modelos descargados en su máquina, mostrando su nombre, tamaño y fecha. Tome una captura de pantalla de esta salida en consola y guárdela como terminal_ollama.png en su carpeta de evidencias. 

   - MD 

2. LM Studio: Abra la aplicación y diríjase a la pestaña Local Server (ícono de doble flecha o servidor en el panel izquierdo). En el menú desplegable superior, verifique que aparezca el modelo cuantizado que descargó (por ejemplo, qwen2.5-coder en formato .gguf ). Tome una captura de esta pantalla demostrando que el entorno está listo, y guárdela como interfaz_lmstudio.png . 

   - MD 

### 2. Ejecución y prueba de los archivos .py 

Para que los scripts funcionen, su entorno de Python debe contar con la librería para manejar peticiones HTTP. Ejecute este comando en su terminal si aún no la tiene instalada: 

#### Bash 

<mark></mark> 

pip install requests 

1. Prueba del endpoint de Ollama ( ollama_test.py ): 

1. Asegúrese de que el servicio de Ollama esté corriendo en segundo plano (debe estar visible en la bandeja del sistema de Windows/macOS). 

2. Abra su terminal, navegue hasta la ruta de la carpeta Componente2 y ejecute: 

Bash python ollama_test.py 

<mark></mark> 

3. Evidencia a capturar: Tome una captura de pantalla de la terminal una vez que el script finalice, mostrando claramente el JSON decodificado, el bloque de código generado por el modelo y el tiempo de respuesta. MD 

2. 

- Prueba del endpoint de LM Studio ( lmstudio_test.py ): 

   1. Dentro de la aplicación LM Studio, en la pestaña Local Server, seleccione su modelo y presione el botón Start Server. El sistema indicará que está escuchando peticiones en http://localhost:1234/v1 . 

   2. Abra una nueva terminal, posicione la ruta en su carpeta Componente2 y ejecute: 

<mark></mark> 

- Bash <mark></mark> python lmstudio_test.py 

- 3. Evidencia a capturar: Necesitará dos capturas aquí. La primera, de su terminal mostrando el script ejecutado correctamente. La segunda, de la ventana de LM Studio, donde la consola interna (Server Logs) mostrará la recepción del método POST /v1/chat/completions y la métrica de tokens procesados por segundo 

- (tok/s). MD 

Estas capturas demostrarán fehacientemente que la cadena arquitectónica Modelo -> Servidor Local -> API -> Aplicación Python se ejecutó con éxito en su entorno local. 

MD 



para lmstudio obtengo esto 

El error que observa en la imagen, donde indica "No results found" y "You have 0 local models", ocurre principalmente por la sintaxis de búsqueda utilizada y la pestaña en la que se encuentra. 

##### PNG 

LM Studio no utiliza el sistema de etiquetas con dos puntos ( : ) propio de Ollama (como qwen2.5-coder:7b ), sino que se conecta al repositorio de Hugging Face y requiere buscar los archivos en formato GGUF. Además, la captura muestra que está buscando dentro de su inventario de modelos locales, el cual está vacío. 

##### PNG + 1 

Para instalar el modelo correctamente en LM Studio y continuar con el entregable, le sugiero seguir estos pasos: 

1. Navegar a la búsqueda global: En la barra vertical del extremo izquierdo, haga clic en el icono de la lupa (Search), no en el icono de la carpeta. 

2. Modificar el término de búsqueda: Escriba Qwen 2.5 Coder 7B GGUF o Qwen2.5Coder-7B-Instruct . Reemplace los dos puntos por espacios o guiones. 

3. Seleccionar el repositorio: Le aparecerán resultados de la comunidad de Hugging Face. Seleccione los repositorios verificados o de usuarios reconocidos como bartowski , lmstudio-community o Qwen . 

4. Elegir la cuantización: Al seleccionar un resultado, en el panel derecho se desplegará una lista de archivos disponibles. Busque y haga clic en Download para la versión Q4_K_M (pesa aproximadamente 4.5 GB). Esta versión de 4 bits es el estándar ideal para no saturar su memoria RAM/VRAM. 

5. Activar la API Local: Una vez finalice la descarga, haga clic en el icono de Local Server (simbolizado con <-> en la barra izquierda). En la parte superior de esa ventana, seleccione el modelo recién descargado, ajuste las configuraciones si lo desea y presione Start Server. 

Con el servidor indicando que está escuchando en el puerto 1234, su archivo lmstudio_test.py ya se ejecutará correctamente, permitiéndole tomar la captura de pantalla necesaria para la carpeta de evidencias. 

si el modelo lo instalé para ollama debo hacer lo mismo en lmstudio, no sería igual para ambos? 

Aunque tanto Ollama como LM Studio ejecutan modelos con arquitectura similar (usualmente cuantizados en formato GGUF), no comparten la misma carpeta de almacenamiento por defecto en su sistema. 

Ollama guarda los archivos en un directorio interno gestionado por sus propios manifiestos de control de versiones, mientras que LM Studio utiliza una carpeta independiente y requiere archivos con la extensión explícita ( C:\Users\jdieg\.lmstudio\models según se observa en la parte inferior derecha de su captura). Por esta razón, lo que usted instala mediante el comando ollama pull no se refleja automáticamente en la biblioteca de LM Studio. 

Para resolver esto y avanzar con su entregable, tiene dos alternativas: 

- Opción 1 (Recomendada y más estable): Descargar el modelo directamente desde la barra de búsqueda global de LM Studio (el ícono de la lupa), siguiendo los pasos del mensaje anterior. Esto garantiza que la herramienta configure correctamente los parámetros del modelo. Además, puede aprovechar este entorno para descargar un modelo distinto (por ejemplo, Phi-3 o Mistral ) y enriquecer la matriz comparativa de su laboratorio con datos más variados. 

- Opción 2 (Importación manual compleja): Usted puede forzar a LM Studio a leer los modelos de Ollama buscando en el directorio de blobs de Ollama. Sin embargo, Ollama elimina la extensión .gguf y renombra los archivos con hashes largos (ej. sha25689b... ). Tendría que copiar ese archivo pesado, pegarlo en la carpeta de LM Studio y renombrarlo manualmente agregando .gguf para que la interfaz lo reconozca. 

Para optimizar su tiempo y evitar errores de compatibilidad en la ejecución de la API local, la descarga independiente a través de la interfaz de LM Studio es el flujo de trabajo adecuado. 

Ahora, pasemos al componente3 

El Componente 3 (Práctica de Vibe Coding: comparación de modelos - 20 %) exige resolver un mismo problema de programación utilizando tres enfoques distintos para observar cómo cambia el ciclo de desarrollo asistido por IA. 

##### MD 

Para cumplir con el requerimiento de un problema pequeño y verificable, utilizaremos la API pública de meteorología (Open-Meteo) con las coordenadas de Manizales. A continuación, le presento la estrategia de ejecución, el prompt base y la plantilla del documento que debe entregar. 

MD 

### 1. El Problema y el Prompt Estandarizado 

Para que la comparación sea metodológicamente válida, debe enviar exactamente la misma instrucción inicial a los tres modelos (Local generalista, Local coding y Cloud coding). 

##### MD 

Copie y pegue el siguiente prompt en sus tres entornos: 

#### Plaintext 

<mark></mark> 

Escribe un script en Python que realice lo siguiente: 

1. Consuma la API pública de Open-Meteo para obtener las temperaturas de los últimos 7 día URL: https://api.open-meteo.com/v1/forecast?latitude=5.0689&longitude=-75.5174&past_day 

2. Valide que la respuesta HTTP sea 200 y que el JSON contenga las llaves 'hourly' y 'temp 3. Cargue los datos en un DataFrame de Pandas, convierta las fechas a formato datetime y v 

4. Calcule e imprima por consola: media, mediana, valor mínimo y valor máximo. 

5. Genere y guarde una gráfica de línea de la temperatura a lo largo del tiempo en un arch Usa tipado estático, manejo explícito de excepciones y añade comentarios técnicos. 

### 2. Flujo de Trabajo (Vibe Coding) 

El documento exige evidenciar el ciclo iterativo de corrección. Usted no debe corregir el código manualmente al primer error; debe pedirle a la IA que lo haga. 

##### MD 

Para cada modelo, documente en su archivo el siguiente flujo: 

MD 

MODELO: (Ej. llama3.1:8b en Ollama). 

- EJECUCIÓN: Al correr el script generado por la IA, ¿qué pasó? (Ej. El script falló con KeyError en la línea 15). 

- CORRECCIÓN: El prompt de ajuste que usted le envió. (Ej. Recibí este error: KeyError 'temperature_2m', por favor corrige la forma en que accedes al diccionario). 

SOLUCIÓN: La cantidad de iteraciones hasta que el código corrió limpiamente. 

### 3. Plantilla para vibe_coding/comparativo.md 

Esta es la estructura Markdown que debe utilizar para su entregable, incorporando estrictamente los criterios de evaluación solicitados. 

##### MD 

Markdown # Comparativo de Vibe Coding 

<mark></mark> 

## 1. Ciclo de Trabajo Documentado 

*(Documente brevemente aquí los prompts correctivos que tuvo que usar para cada modelo hasta llega 

## 2. Matriz Comparativa 

- | Criterio | Local Generalista (ej. Llama 3.1 8B) | Local Coding (ej. Qwen 2.5 Coder 7B) | | :--- | :--- | :--- | :--- | 

- | **Código ejecutable** | *(Ej: No al primer intento, falló en importaciones)* | *(Ej: Sí, ejecutó co | **Errores encontrados** | *(Describa las excepciones de Python observadas)* | *(Describa fallo | **Iteraciones necesarias** | *(Ej: 3 iteraciones)* | *(Ej: 1 iteración)* | *(Ej: 0 iteraciones)* | | **Tiempo hasta solución** | *(Ej: 8 minutos)* | *(Ej: 3 minutos)* | *(Ej: 1 minuto)* | | **Calidad/claridad del código**| *(Ej: Estilo inconsistente, falta tipado)* | *(Ej: PEP 8 respetad | **Documentación** | *(Ej: Exceso de texto explicativo)* | *(Ej: Comentarios precisos en línea)* | 

| **Pruebas sugeridas/generadas**| *(Ej: Ninguna)* | *(Ej: Sugirió bloque try/except)* | *(Ej: Gen | **Intervención humana necesaria**| *(Ej: Alta, para depurar la estructura JSON)* | *(Ej: Baja, s 

## 3. Reflexión Técnica 

*(Redacte aquí un párrafo concluyendo qué cambió en su experiencia como ingeniero al variar el tipo 

Para asegurar que los resultados de la IA sean correctos, ¿considera útil que le proporcione el script base en Python con la solución exacta de este problema para que usted tenga un punto de comparación objetivo frente a lo que generen los modelos? 

sugiéreme qué modelos puedo usar 

Para cumplir con las tres categorías exigidas en la comparación de Vibe Coding del Componente 3, le sugiero las siguientes combinaciones optimizadas para ejecutarse fluidamente en hardware local y ofrecer un contraste claro en la generación del script de Python. 

MD 

#### 1. Modelo Local Generalista 

#### Opción principal: Llama 3.1 (8B) 

Por qué elegirlo: Es el estándar actual para tareas generales. Tiene un razonamiento lógico sólido, pero al no estar purificado exclusivamente para programación, le dará el contraste perfecto para documentar errores típicos de sintaxis o importaciones, cumpliendo el propósito del laboratorio. 

MD 

Ejecución en Ollama: ollama run llama3.1 

Alternativa: Gemma 2 (9B) 

Por qué elegirlo: Modelo de Google con excelente rendimiento general, útil si desea variar la comparativa. 

Ejecución en Ollama: ollama run gemma2 

#### 2. Modelo Local Especializado en Código 

#### Opción principal: Qwen 2.5 Coder (7B) 

Por qué elegirlo: Actualmente lidera las métricas de rendimiento en modelos locales de 7 a 8 billones de parámetros. Genera scripts limpios, maneja el tipado estricto adecuadamente y comprende muy bien librerías de datos como Pandas. 

Ejecución en Ollama: ollama run qwen2.5-coder:7b 

   - Búsqueda en LM Studio: Qwen2.5-Coder-7B-Instruct GGUF (versión Q4_K_M). 

- Alternativa: DeepSeek Coder (6.7B o V2 Lite) 

   - Por qué elegirlo: Muy estable para arquitecturas backend, manejo de excepciones y consumo de APIs. 

Ejecución en Ollama: ollama run deepseek-coder:6.7b 

#### 3. Modelo de Desarrollo Cloud 

#### Opción principal: Claude 3.5 Sonnet 

Por qué elegirlo: Es ampliamente reconocido como el modelo más capaz para desarrollo de software en la actualidad. Supera a la mayoría en precisión arquitectónica y manejo de dependencias. Puede usarlo sin costo desde su interfaz web para pasarle el prompt. 

#### Alternativa: GitHub Copilot / GPT-4o 

Por qué elegirlo: Si tiene validado el paquete de beneficios de GitHub Educación con su correo universitario, Copilot le brinda acceso directo a modelos de OpenAI directamente en su editor. En su defecto, interactuar con GPT-4o desde ChatGPT cumple sobradamente con el requerimiento de un modelo cloud avanzado. MD 

Estrategia de ejecución: 

Seleccionar Llama 3.1 (Generalista), Qwen 2.5 Coder (Coding) y Claude 3.5 Sonnet (Cloud) le garantizará respuestas con niveles de madurez técnica muy distintos. Esto facilitará enormemente el diligenciamiento de la matriz comparativa, ya que el modelo generalista probablemente requerirá iteraciones correctivas, el especializado funcionará con ajustes mínimos, y el cloud entregará una solución lista para producción. 

MD 

|TXT|TXT|TXT|
|---|---|---|
|respuestallam<br>a3.1|respuestaQwe<br>n2.5|respuestaSon<br>net5|



Te adjunto las 3 respuestas de cada modelo, construye la plantilla comparativa solicitada 

# Comparativo de Vibe Coding 

## 1. Ciclo de Trabajo Documentado 

Llama 3.1 8B (Local Generalista): El modelo generó un script procedimental de un solo bloque. Ignoró la instrucción de utilizar tipado estático y usó un manejo de excepciones básico con assert . Para que alcance el nivel solicitado, requeriría un prompt correctivo: "Reescribe el código usando funciones separadas, aplica tipado estático estricto (typing) como se pidió inicialmente y no uses assert para la lógica de validación HTTP". 

TXT + 1 

Qwen 2.5 Coder (Local Coding): El modelo estructuró la solución en funciones modulares e implementó el tipado estático ( Dict , Any , pd.DataFrame ) desde el primer intento. Realizó las validaciones HTTP y de llaves JSON con condicionales if explícitos. No requeriría iteraciones adicionales de prompt, salvo pedirle que encapsule la ejecución final en un bloque if __name__ == "__main__": . 

TXT + 1 

Claude 3.5 Sonnet (Cloud Coding): Entregó un script con calidad de producción (zeroshot). Incluyó configuración de backend sin interfaz gráfica ( matplotlib.use("Agg") ) para evitar bloqueos al guardar la imagen, estructuró constantes globales y manejó excepciones específicas como RequestException y OSError . Cero iteraciones necesarias. 

TXT + 1 

## 2. Matriz Comparativa 

|Criterio|Local Generalista|Local Coding (Qwen|Cloud Coding (C|
|---|---|---|---|
||(Llama 3.1 8B)|2.5 Coder 7B)|3.5 Sonnet)|
|Código ejecutable|Sí, pero es un script lineal<br>procedimental.|Sí, estructurado en<br>funciones modulares.|Sí, altamente robu<br>bloque<br>main() .|
||TXT|TXT|TXT|
|Errores encontrados<br>Iteraciones necesarias|Ignoró por completo el<br>requerimiento de tipado<br>estático.<br>TXT<br>1 a 2 iteraciones (para|Ningún error sintáctico;<br>levanta<br>Exception<br>genéricas en lugar de<br>tipos específicos.<br>TXT<br>0 a 1 iteración (para|Ninguno. Anticipó<br>el error de entorno<br>gráfico de matplo<br>TXT<br>0 iteraciones. Solu|
||refactorizar a funciones y<br>añadir tipado).|ajustes menores de estilo<br>o bloque main).|lista para producc<br>TXT|
|Tiempo hasta solución|Medio (requiere<br>intervención para cumplir<br>todos los requisitos).|Bajo (cumple casi todo al<br>primer intento).|Mínimo (ejecució<br>inmediata).|



|Criterio|Local Generalista<br>(Llama 3.1 8B)|Local Coding (Qwen<br>2.5 Coder 7B)|Cloud Coding (C<br>3.5 Sonnet)|
|---|---|---|---|
|Calidad/claridad del|Aceptable, pero mezcla|Alta, separa|Excelente, usa con|
|código|lógica de consumo,<br>validación y gráfica en el|responsabilidades en 4<br>funciones claras y aplica|tipadas, docstring<br>detallados y forma|
||flujo principal.|tipado<br>typing .|salida de consola.|
||TXT|TXT|TXT|
|Documentación|Comentarios en línea<br>básicos y explicación|Comentarios precisos<br>antes de cada bloque|Nivel profesional,<br>descripción del m|
||conversacional al final.<br>TXT|lógico dentro de las<br>funciones.<br>TXT|requisitos y docst<br>por función.<br>TXT|
|Pruebas|Valida la existencia de|Valida campos y nulos|Validación explícit|
|sugeridas/generadas|campos y nulos usando<br>aserciones (<br>assert ).|con condicionales<br>ify<br>levanta excepciones si|status_code ,<br>validación de JSO|
||TXT|fallan.<br>TXT|imprime conteo e<br>de nulos.<br>TXT|
|Intervención humana<br>necesaria|Moderada (para<br>refactorizar y añadir<br>tipos).<br>TXT|Baja (solo ejecutar e<br>instalar dependencias).<br>TXT|Nula (código listo<br>ejecutar).<br>TXT|



## 3. Reflexión Técnica 

La transición entre los tres modelos evidencia claramente el impacto de la especialización en el desarrollo de software. El modelo generalista (Llama 3.1) resuelve la lógica fundamental de Pandas y Requests, pero falla en la arquitectura del código al ignorar directivas clave como el tipado estricto, prefiriendo un enfoque procedimental básico. Al pasar a un SLM especializado en código (Qwen 2.5), la IA demuestra una comprensión nativa de las buenas prácticas de ingeniería, modularizando la solución y aplicando tipos automáticamente sin consumir más recursos locales. Finalmente, el modelo Cloud (Claude 3.5 Sonnet) expone la diferencia entre "escribir un script que funcione" y "desarrollar software robusto", anticipando problemas de infraestructura (como la configuración del backend gráfico de Matplotlib) y manejando jerarquías de excepciones complejas que garantizan la resiliencia de la aplicación en producción . El ingeniero deja de ser un simple escritor de sintaxis para convertirse en un revisor y orquestador de componentes. 

TXT + 2 

dame el contenido .md de la matriz para adjuntarla dentro de la documentación 

> Markdown <mark></mark> 

# Comparativo de Vibe Coding 

## 1. Ciclo de Trabajo Documentado 

* **Llama 3.1 8B (Local Generalista):** El modelo generó un script procedimental de un s 

* **Qwen 2.5 Coder (Local Coding):** El modelo estructuró la solución en funciones modul 

* **Claude 3.5 Sonnet (Cloud Coding):** Entregó un script con calidad de producción (zer 

## 2. Matriz Comparativa 

| Criterio | Local Generalista (Llama 3.1 8B) | Local Coding (Qwen 2.5 Coder 7B) | Cloud C | :--- | :--- | :--- | :--- | 

| **Código ejecutable** | Sí, pero es un script lineal procedimental[cite: 6]. | Sí, estru | **Errores encontrados** | Ignoró el requerimiento de tipado estático[cite: 6]. | Ningún 

| **Iteraciones necesarias** | 1 a 2 iteraciones (refactorizar y añadir tipado). | 0 a 1 i 

| **Tiempo hasta solución** | Medio. | Bajo. | Mínimo. | 

| **Calidad/claridad del código**| Aceptable, pero mezcla lógica de consumo, validación y | **Documentación** | Comentarios en línea básicos[cite: 6]. | Comentarios precisos antes | **Pruebas sugeridas/generadas**| Valida existencia de campos y nulos usando `assert`[cit 

| **Intervención humana necesaria**| Moderada (para refactorizar y añadir tipos)[cite: 6]. 

## 3. Reflexión Técnica 

La transición entre los tres modelos evidencia el impacto de la especialización en el desa 

