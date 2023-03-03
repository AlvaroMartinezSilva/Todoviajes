from bs4 import BeautifulSoup
import requests
import os
from io import open
import json


counter_dictionary={}



def veinteminsParrafos(soup):
  content = ""
  #buscamos el div de la class donde se encuentra todo el cuerpo del artículo
  text = soup.find("div", class_="article-text")
  # buscar todos los p
  paragraphs = text.find_all("p")
  # sacar el texto del p y anadir al content
  for paragraph in paragraphs:
      content = content + paragraph.text + "\n"
  return content




def veinteminsWebScraping(pagina, tipo_periodico, categoria):

  soup = BeautifulSoup(pagina, 'html.parser')



  texto = veinteminsParrafos(soup)




  return texto



def veintemins(periodico, tipo_periodico, categoria, url):
  counter_dictionary[categoria] = {}
  pagina = requests.get(url)
  soup = BeautifulSoup(pagina.content, 'html.parser')

 
  data=[]

  # sacar todas los enlaces de los articulos de la pagina categorial
  enlaces = []
  for article in soup.find_all("article"):
      enlaces.append(article.find("a")['href'])

  # processar cada articulo
  for enlace in enlaces:
      articulo = requests.get(enlace)
      # veinteminsWebScraping(articulo. content, tipo_periodico, categoria)
      try:
          result=veinteminsWebScraping(articulo.content, tipo_periodico, categoria)

          data.append(result)
          print("agregando" + enlace)
      except:
        print("Error procesando articulo, saltando el articulo " + enlace)
      
  return data

  

def principal20mins(municipio):
  periodico="https://20minutos.es"
  tipo_periodico="20minutos"

  municipio=municipio.replace(" ","-")
  # processar las categorias: salud, ciencia y tecnologia
  categoria = municipio
  url ="https://20minutos.es/"+municipio.lower()+"/"
  data=veintemins(periodico, tipo_periodico, categoria, url)
  
  return data

