from os import listdir
import os
import time
from os import remove
from os.path import isfile, isdir
import re
import pytube
import moviepy.editor as mp
import re
#Mediante API
import requests
import json
#Mediante Scrapping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from parsel import Selector

def list_and_filt (ruta):
    contenido = listdir(ruta)
    print("Procesando directorio...")
    with open("songs.txt", "w", encoding="UTF-8") as f:
        for i in contenido:
            i= i.replace(".mp3", "").replace(".wav", "").replace(".acc", "").replace("MP3_128K","").replace("MP3_70K","")
            i = re.sub("[.@-]", "", i)
            f.write(i+"\n")
        f.close()
    print("Procesado [OK]")

def download_and_convert_song(url,name):
    
    path = "XXX" #Ruta del directorio donde se descargaran los archivos
    if not (os.path.isdir(path)):
        os.mkdir(path)

    try:
        print("Descargando")
        stream = pytube.YouTube(url).streams.filter(subtype='mp4').first()
        stream.download(path,filename= name)
        time.sleep(5)
        print("Convirtiendo a mp3 320kbps..")
        clip = mp.VideoFileClip(path+ name +'.mp4')
        #Lo escribimos como audio y '.mp3'
        clip.audio.write_audiofile(path+name+".mp3", bitrate="320k")
        clip.close()
        time.sleep(5)
        remove(path+name+".mp4")
        print("Completado")
    except Exception as e:
        print(e)

#Mediante selenium
def obtener_link(filename):

    opts = Options()
    opts.add_argument("--headless")
    lista_links=""
    driver = webdriver.Chrome("C:/Windows/chromedriver", options=opts) ##Editar ruta en caso de que la ruta sea distinta.
    with open(filename, "r", encoding="UTF-8") as f:
        for linea in f:  
            try:
                    linea = linea.replace(" ", "+")
                    base_url = "https://www.youtube.com"

                    url = 'https://www.youtube.com/results?search_query=' + linea
                    driver.get(url)

                    sel = Selector(driver.page_source)
                    primer_resultado = sel.xpath('//div/h3/a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]/@href').extract_first()
                    lista_links += base_url + primer_resultado +"\n"
            except Exception as e:
                print(e)
    driver.close()

    return lista_links

#Mediante la Api v3 de Youtube Data
def obtener_link_API(query, limit=2):

    API_KEY = "XXXX" #Introduzca su API KEY (V3 only)
    url = f"https://www.googleapis.com/youtube/v3/search"
    data = {
        "key": API_KEY,
        "part": "id,snippet",
        "q": query,
        "max_results": limit
    }
    r = requests.get(url, params=data)
    j = r.json()
    # Construir y retornar lista simplificada
    return [ (v["id"]["videoId"], v["snippet"]["title"]) for v in j["items"] ]
    

def manage():

    list_and_filt('XXXX') #Ruta del directorio donde se encuentran los archivos de los cuales se realizara la busqueda
    list_urls=""
    list_urls = obtener_link("songs.txt")
    #Para utilizar con obtener link con API de Google
    #resultados = obtener_link_API(linea)
    #url = "https://www.youtube.com/watch?v={}".format(resultados[0][0])
    #print(list_urls)

    #Guarda las urls en un archivo txt
    with open("urls.txt","w",encoding="UTF-8") as urls:
        for y in list_urls:
            urls.write(y)
        urls.close()
    
    #lee el archivo de urls y el de nombres, descarga y convierte las canciones asignandoles el nombre inicial
    with open("urls.txt", "r", encoding="UTF-8") as urls, open('songs.txt', 'r', encoding="UTF-8") as names:
        for url,name in zip(urls,names) :
            try:
                download_and_convert_song(url,name)
            except Exception as e:
                print(e)
        urls.close()
        names.close()
    
def main():
    manage()

if __name__ == "__main__":
    main()