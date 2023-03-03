from bs4 import BeautifulSoup
import requests
import os
import json
from io import open



counter_dictionary={}


def elMundoPalabrasLlaves(soup):
  palabras_llaves = ""
  separador = ", "
  # listo con todos los palabras llaves
  html_llaves = soup.find("ul", class_="ue-c-article__tags ue-l-article--leftcol-width-from-desktop ue-l-article--float-left-from-desktop ue-l-article--move-to-leftcol-from-desktop ue-l-article--bottom-absolute-from-desktop")
  # solo los palabras que son enlaces
  enlaces_llaves = html_llaves.find_all("a")
  # sacar el texto del enlace y anadir al listo de todos
  for enlace in enlaces_llaves:
      palabras_llaves = palabras_llaves + enlace.text + separador
  # quitar ultima seperador
  palabras_llaves = palabras_llaves[:-(len(separador))]
  return palabras_llaves


def elMundoTexto(soup):
  content = ""
  # div con todo el texto
  text = soup.find("div", class_="ue-l-article__body ue-c-article__body")
  # buscar todos los p
  #ue-l-article__body ue-c-article__body
  paragraphs = text.find_all("p")
  # sacar el texto del p y anadir al content
  for paragraph in paragraphs:
    content = content + paragraph.text + "\n"
  # print(content)
  return content


def elMundoTitulo(soup):
  return soup.find("h1", class_="ue-c-article__headline js-headline").text



def elMundoEntradilla(soup):
  return soup.find("p", class_="ue-c-article__standfirst").text

def elMundoFecha(soup):
  date_length = 10 # 2021-12-03T18:09:39.529Z
  time=soup.find("time")
  return time.get('datetime')[:date_length]


def elMundoWebScraping(pagina, diario_texto, categoria):
  soup = BeautifulSoup(pagina, 'html.parser')

  palabras_llaves = elMundoPalabrasLlaves(soup)
  titulo = elMundoTitulo(soup)
  entradilla = elMundoEntradilla(soup)
  texto = elMundoTexto(soup)
  fecha = elMundoFecha(soup)

  return titulo,entradilla,texto,palabras_llaves,fecha



def elMundo(diario_texto, categoria, url):
  counter_dictionary[categoria] = {}
  pagina = requests.get(url)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  
  data=[]


  enlaces = []

  for article in soup.find_all("article"):
      enlaces.append(article.find("a")['href'])

  for enlace in enlaces:
      articulo = requests.get(enlace)
      try:

        result=elMundoWebScraping(articulo.content, diario_texto, categoria)

        data.append(result[2])

        print("agregando" + enlace)

      except:
          print("articulo premium saltando" + enlace)


  return data



def principalelMund(municipio):

  diario_texto = "elMundo"
  counter_dictionary = {}


  municipio=municipio.replace(" ","-")
  categoria = "municipio"
  print(municipio.lower())
  url = "https://www.elmundo.es/"+municipio.lower()+".html"
  print(url)
  dato=elMundo(diario_texto, categoria, url)
  return dato











