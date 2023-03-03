from bs4 import BeautifulSoup
import requests
import os
import json

# El Pais



def elPaisPalabrasLlaves(soup):
  palabras_llaves = ""
  separador = ", "
  # Hacemos un lista con las palabras llave
  html_llaves = soup.find("ul", class_="_df _ls")
  # Solo extraemos los enlaces
  enlaces_llaves = html_llaves.find_all("a")
  # Sacamos el texto de los enlaces y y lo añadimos a la lista
  for enlace in enlaces_llaves:
      palabras_llaves = palabras_llaves + enlace.text + separador
  # Quitamos el ultimo separador
  palabras_llaves = palabras_llaves[:-(len(separador))]
  return palabras_llaves

def elPaisTexto(soup):
  content = ""
  # div con todo el texto
  text = soup.find("div", class_="a_c")
  # buscar todos los p
  paragraphs = text.find_all("p")
  # Sacamos el contenido de p y lo añadimos a content
  for paragraph in paragraphs:
      content = content + paragraph.text + "\n"
  # print(content)
  return content

def elPaisTitulo(soup):
  return soup.find("h1", class_="a_t").text

def elPaisEntradilla(soup):
  return soup.find("h2", class_="a_st").text

def elPaisFecha(soup):
  date_length = 10 # 2021-12-03T18:09:39.529Z
  return soup.find("a", id="article_date_p")["data-date"][:date_length]


def elPaisWebScraping(pagina, diario_texto, categoria):
  soup = BeautifulSoup(pagina, 'html.parser')

  palabras_llaves = elPaisPalabrasLlaves(soup)
  titulo = elPaisTitulo(soup)
  entradilla = elPaisEntradilla(soup)
  texto = elPaisTexto(soup)
  fecha = elPaisFecha(soup)



  return titulo,entradilla,texto,palabras_llaves,fecha

def elPais(diario, diario_texto, categoria, url):

  counter_dictionary[categoria] = {}
  pagina = requests.get(url)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  data=[]

  # sacar todas los enlaces de los articulos de la pagina categorial
  enlaces = []
  for article in soup.find_all("article"):
      enlaces.append(diario + article.find("a")['href'])

  # processar cada articulo
  for enlace in enlaces:
      articulo = requests.get(enlace)
      try:
        result=elPaisWebScraping(articulo.content, diario_texto, categoria)

        data.append(result[2])
        print("agregando" + enlace)
      except:
          print("Error procesando articulo, saltando el articulo " + enlace)
  return data




counter_dictionary={}

def principalelPais(municipio):
  # processar las categorias: salud, ciencia y tecnologia


  diario = "https://elpais.com"
  diario_texto = "elPais"
  counter_dictionary = {}


  municipio=municipio.replace(" ","_")

  categoria = municipio.lower()

  url ="https://elpais.com/noticias/"+municipio.lower()
  data =elPais(diario, diario_texto, categoria, url)
  return data