# Youtube-List-Get-Links-Download-Convert
Este script lee un directorio obteniendo de ahí, los nombres de los archivos y volcanolos en un .txt, después mediante web scrapping obteniene los links de dichas canciones, las descarga y convierte a mp3 con un bitrate de 320kbps.

## Requisitos

* [Python3](https://www.python.org/download/releases/3.0/).

* Librerias : ```python -m pip install -r requirements.txt``` (En el directorio del codigo)

* Chrome Webdriver: Descarguelo desde aquí: https://chromedriver.chromium.org/downloads
  Después de eso, descomprimalo y coloquelo en el directorio "C:/Windows/"
  
* (Opcional) API V3 de Youtube: puedes obtenerla mediante este tutorial: https://programacion.net/articulo/como_obtener_una_clave_para_la_youtube_data_api_1844

## Configuración 🔧

Modifique todos los parámetros en el código (normalmente expresado como "xxxx ..."), guíese de acuerdo con los comentarios.

## Diseño

Se ha utilizado:

* Pytube: Sirve para descargar videos de Youtube

* Json: Procesar los resultados de la API de Youtube

* API V3 de Youtube: Se emplea para hacer peticiones a Youtube, utilizando su propia API,

* Selenium: Para obtener los links a raiz de una cancion , se hace una busqueda mediante web-scrapping.

* Moviepy: Se emplea para convertir un archivo de un formato a otro, ejemplo: .mp4 a .mp3

* Parsel: Libreria que se usa para extraer informacion de Xml, Html, XPath y CSS.

## Ejecución

 ```py -u "converty_to_320.py"```
 
  ## Autor ✒️

* **Jorge Manuel Lozano Gómez**
