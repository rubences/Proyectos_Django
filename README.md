# Proyectos_Django
Proyectos Django para varias asignaturas actualizado para lectura de datos y LLM


# La automatización de Django es real: elimina el exceso de código
La automatización y la abstracción van de la mano. En el caso de Django, las abstracciones funcionan para reducir la escritura que tienes que hacer. Comenzando desde la creación de archivos para proyectos y aplicaciones, y completando la configuración del servidor, hasta el posicionamiento de las etiquetas html en el front-end usando DTL, hay muchos lugares que Django automatiza y abstrae. 

Si navega por el sitio, contiene aproximadamente 210 páginas. Las páginas se crearon a partir de componentes como base, encabezados, pies de página y partes principales de HTML. Hay 5 scripts de Python y unas 8 páginas HTML que funcionan juntas para construir el sitio completo. Django también extiende la abstracción al frente HTML. Estos componentes se combinaron con datos de la base de datos, imágenes almacenadas en servidores y enlaces generados utilizando lenguaje DTL. Todo esto conduce a muy menos código y páginas html.

# Django gestiona la gestión de usuarios: elimina el código de acceso
Ya sea Flask, FastAPI o Express, todos estos marcos requieren que la administración de usuarios, los tokens de acceso y el proceso de registro se codifiquen cada vez que se crea una aplicación web. Lo que lleva tiempo y complica las cosas para los alumnos. Integrarlo con todo el sitio web y alojarlo en una plataforma también puede resultar un desafío. Django proporciona modelos de usuario y un panel de administración como baterías incluidas con el proyecto. Para acceder al inicio de sesión, a la página de registro, login.html y el formulario en Register.html deben colocarse en la carpeta de plantillas.

Formularios y modelos de bases de datos: elimina la creación de formularios
Forms resuelve el problema de recopilación de datos. Obtienen los datos del usuario y los utilizan para la lógica interna o para almacenar los datos en la base de datos. Cuando los datos se van a almacenar directamente en la base de datos, los formularios de Django pueden ampliar directamente los modelos de las tablas de la base de datos. La página del formulario html se representa llamando a la variable de formularios desde el backend.

Cuando el formulario se utiliza para recopilar información para proporcionar cierta información al usuario, pasándola a través de las vistas y el controlador, el objeto de solicitud contiene toda la información, desde el Usuario, el Método y su acción de formulario asociada. Cada uno de estos se puede extraer fácilmente en las vistas y la lógica se puede escribir con facilidad.

# Etiquetas estáticas y otras etiquetas DTL: elimina el desorden
Una característica notable de Django es la variable ESTÁTICA que proporciona acceso a datos o archivos dentro del disco duro del servidor. Hacer esto a través de la abstracción orientada a objetos hace posible usarlo en todo el marco de Django. Comenzando con la configuración hasta que los datos se representen en el front-end. Static ayuda a crear páginas HTML a partir de los componentes, agregando imágenes y archivos CSS de carpetas en el directorio estático.

Si es necesario construir la interfaz con dos marcos CSS diferentes, Bulma/Bootstrap… siéntete libre. Dado que el backend aparentemente se fusionará con ambos. Eso también se puede hacer con el mínimo tiempo y esfuerzo. Gracias a las carpetas estáticas. Administrar el código base se vuelve más fácil y controlar la seguridad es muy sencillo.

# Carga de datos con scripts: elimina comandos SQL
La carga de datos es tediosa, todos estamos de acuerdo. Con las extensiones de Django viene runscript, que ejecuta los scripts que pueden cargar datos en la base de datos mediante bucles pitónicos. Ya sea una integración con BigData o pequeños archivos CSV, los bucles pitónicos finalmente acceden a los modelos de bases de datos como objetos Python y guardan los datos. No es necesario escribir una consulta de inserción SQL para cargar los datos. Incluso toda la base de datos se abstrae como back-end, ya que Django escribe la consulta a la base de datos.

# Planteamiento del problema:

Cree un sitio web de blog que incluya una opción de búsqueda que implemente la búsqueda vectorial utilizando modelos de incrustación de código abierto.

# Ingredientes:
Se instalarán bibliotecas de Django, langchain, faiss y transformadores de oraciones.
Cree la base de datos Faiss con vid_id, título y descripción incrustados
Cree la aplicación y conecte las funciones de vistas y URL.
Utilice bootstrap y DTL para construir la interfaz. El ejemplo de Jumbotron en bootstrap es el más adecuado para el proyecto

# Desafíos resueltos: Parte 1
Lo difícil es llevar los datos proporcionados por la búsqueda vectorial al frontend. Aunque hay que admitir DTL, el diseño de la página aún debe arreglarse primero y debe construirse de forma modular. Django proporciona la abstracción para construir las páginas y modificar sus partes mediante programación.

El primer paso es dividir los enlaces del encabezado, pie de página y hoja de estilo y ensamblarlos dentro del archivo base.html. Una vez logrado esto, el cuerpo podrá construirse parte por parte. El HTML lo proporciona bootstrap. El problema es tomar el alcance de las etiquetas que colocan los datos en la página y mantener el estilo.

https://youtu.be/cGw8Ti7no2k

# Desafíos resueltos: Parte 2
Antes de finalizar los modelos para las tablas de la base de datos, es necesario revisar la estructura de los datos sin procesar. Esto ayudará a automatizar la carga de datos más fácilmente. Datos desordenados del mundo real o big data estructurados, se debe acceder a los puntos de datos uno por uno para cargarlos en la base de datos. Además de cargar los datos en la base de datos, también necesitamos cargar los mismos datos en Vector Database.

Discutimos cómo crear una base de datos vectorial FAISS utilizando los datos de YouTube que están disponibles en el siguiente enlace. Luego ejecute una búsqueda de similitudes en las descripciones incrustadas. https://youtu.be/g8DGwp97ocU

Los datos y el código se encuentran en https://www.kaggle.com/code/kamaljp/youtube-data-extraction


# Desafíos resueltos: Parte 3
Presenté que el front-end se construirá usando Bootstrap. Tenemos que aprender a descomponer una sola página en muchas partes. Luego, cómo integrar las partes en diferentes páginas usando el lenguaje de plantillas de Django y las carpetas de plantillas. El vídeo a continuación explica este proceso comenzando con la página html de Jumbotron. https://youtu.be/G0lxdRG0ulI



# Desafíos resueltos: Parte 4

Tenemos lista la base de datos vectorial y la plantilla de front-end. Lo siguiente es completar los datos devueltos por la base de datos de vectores. Las funciones de vistas se utilizan para consultar la base de datos y enviar los resultados. El DTL utiliza el contexto de la ruta de la URL para completar el frente. La parte 4 del siguiente vídeo te guía claramente a través de esa parte. https://youtu.be/lrOSstwUVKM

# Parte 5: Olvídese de Langchain, utilice https://www.griptape.ai/ en su lugar

¿Qué es Langchain?
Langchain es un SDK escrito en Python que facilita la integración de modelos de lenguaje grandes en aplicaciones de IA personalizadas. Elimina la complejidad de trabajar directamente con LLM como GPT-3, lo que permite a los desarrolladores centrarse en crear la lógica de su sistema.


# Algunas características clave de Langchain incluyen:

Soporte para los principales LLM como GPT-3.5, GPT-4, T5, Codex y más.
Módulos de memoria que le permiten pasar memoria a largo plazo entre solicitudes
Capacidades de encadenamiento para conectar múltiples consultas de modelos juntas
Arquitectura modular para intercambiar componentes.
Integraciones prediseñadas con bases de datos, motores de búsqueda y más
Código abierto con una comunidad activa
Con Langchain, los desarrolladores han utilizado LLM para crear chatbots de respuesta a preguntas, resumir texto, clasificar contenido, traducir entre idiomas y mucho más. Es uno de los proyectos de IA de código abierto de más rápido crecimiento.

# Presentamos Griptape.ai
Griptape.ai ofrece un enfoque alternativo como marco de Python diseñado para el desarrollo de aplicaciones empresariales de IA. Proporciona estructura y herramientas diseñadas para la preparación para la producción.


Estas son algunas de las características destacadas de Griptape.ai:

Componentes modulares para mayor flexibilidad
Herramientas de configuración para gestionar modelos.
Integración con fuentes de datos como SQL, NoSQL, S3
Editor de flujo de trabajo para visualizar la lógica de un extremo a otro
Controles de seguridad avanzados y gestión de acceso
Características de gobernanza del modelo
Opciones de soporte comercial
Si bien Langchain simplifica la consulta de modelos de lenguaje grandes, Griptape le brinda más control sobre todo el ciclo de vida y la infraestructura de una aplicación de IA.

Diferencias clave entre Langchain y Griptape.ai
1. Arquitectura
Langchain tiene una arquitectura encadenada que pasa entradas y salidas entre componentes. Griptape utiliza una estructura de gráfico acíclico dirigido (DAG) con nodos y enlaces. Esto proporciona más flexibilidad en el diseño de flujos de trabajo complejos.

2. LLM como servicio
Langchain se centra exclusivamente en simplificar la integración de LLM. Griptape opera más cerca de un modelo "LLM como servicio" con características como gestión y optimización de modelos.

3. Diseñado para escalar
Langchain permite la creación rápida de prototipos, mientras que Griptape está optimizado para la escalabilidad con herramientas de producción.

4. Integración de datos
Langchain confía en sus módulos de memoria. Griptape utiliza conectores en vivo para fuentes de datos como bases de datos y almacenes de objetos.

5. Seguridad
Como proyecto de código abierto, Langchain deja la seguridad en manos del usuario. Griptape tiene controles de acceso nativos, cifrado y otras funciones de seguridad.

6. Soporte Comercial
Langchain está impulsado por la comunidad. Griptape ofrece soporte empresarial y servicios profesionales.

7. Personalización
Langchain tiene una arquitectura modular. Pero Griptape permite integrar una lógica personalizada en cualquier punto de los flujos de trabajo de la aplicación.

# ¿Cuándo debería utilizar Griptape en lugar de Langchain?
Para muchos proyectos de prueba de concepto o experimentos de bajo riesgo, Langchain proporciona una excelente puerta de entrada para aprovechar grandes modelos de lenguaje. Pero para los equipos empresariales que crean aplicaciones críticas para el negocio, Griptape.ai tiende a ser más adecuado debido a su enfoque en el control, la gobernanza y la confiabilidad.

A continuación se muestran algunos ejemplos de casos en los que Griptape puede ser preferible a Langchain:

Datos altamente confidenciales : servicios financieros, atención médica u otras industrias altamente reguladas donde la protección de datos es fundamental.
Aplicaciones de misión crítica : cualquier sistema donde el tiempo de inactividad afectaría significativamente las operaciones o los ingresos.
Muchos datos no estructurados : aplicaciones que involucran grandes volúmenes de datos en tiempo real de diversas fuentes.
Necesidad de personalización : casos de uso complejos que requieren una profunda personalización de la lógica y el flujo de trabajo de la aplicación.
Escalado a producción : transición de la experimentación a aplicaciones de producción completa.
Casos de uso de Griptape.ai
Con sus funciones orientadas a la empresa, Griptape.ai se presta bien a aplicaciones sofisticadas en muchas industrias:

Servicios financieros
Los bancos utilizan Griptape para crear asistentes de inteligencia artificial para el servicio al cliente, la detección de fraudes a partir de datos de transacciones, información sobre inversiones a partir de noticias y más.

comercio electrónico
Griptape puede impulsar recomendaciones de productos, relevancia de búsqueda, segmentación de clientes y otras aplicaciones para mejorar el comercio minorista en línea.

Cuidado de la salud
Desde el apoyo a las decisiones clínicas hasta los conocimientos de investigación, Griptape ayuda a las organizaciones de atención médica a aprovechar la IA mientras protege los datos de los pacientes.

Energía
Las empresas de servicios públicos emplean Griptape para pronosticar la demanda, realizar mantenimiento predictivo, optimizar la producción de energía y reducir los cortes de riesgo.

Medios y entretenimiento
Con Griptape es posible generar subtítulos de vídeo automatizados, producir gráficos por computadora, remezclar contenido y personalizar recomendaciones.

Estos son solo algunos ejemplos. Prácticamente cualquier empresa que necesite crear aplicaciones de IA personalizadas puede beneficiarse del enfoque único de Griptape.ai.

# Comparación de funciones de Griptape.ai y Langchain
CaracterísticaLangchainGriptape.aiArquitecturaEncadenadoLLM basados ​​en gráficos (DAG)Integraciones”LLM como servicio“EnfoquePrototiposConectores de datos listos para producciónMódulos de memoriaLive SQL, NoSQL, etc.SeguridadAdministrado por el usuarioControles de acceso, cifradoSoporte comercialComunidadPlanes de soporte empresarialPersonalizaciónMódulosCualquier paso en el flujo de trabajo

