


from bs4 import BeautifulSoup
import requests



counter_dictionary = {}


def comunidadesmenu():

  linpagA="https://www.minube.com/a/subloc/p/63/all"
  pagina = requests.get(linpagA)
  soup = BeautifulSoup(pagina.content, 'html.parser')
 

  Lmunicipios={}
  Lmunicipios["muni"]=[]
  Lpoblacion=[]
  for poblacion in soup.find_all("div", class_="baseCard riverCard locationCard gridCard"):



    enlace=poblacion.find("a",class_="titleItem")['href']
    prtpob=poblacion.find("a",class_="titleItem").getText()

  
 


    pagina = requests.get(enlace)
    soup = BeautifulSoup(pagina.content, 'html.parser')


    apartado=soup.find("div", class_="title link")

    if apartado==None:
      Lenlaces,Lpoblacion=listapoblacpocas(enlace)
    else:
      Lenlaces,Lpoblacion=listapoblaciones(apartado.get('onclick').split("'")[1])


    buff=prtpob.replace("\n","")
    prtpob=buff[1:len(prtpob)]



    cont=0
    for pov in Lpoblacion:
      buff=pov.replace("\n","")
      pov=buff[1:len(pov)]

      pagina = requests.get(Lenlaces[cont])
      soup = BeautifulSoup(pagina.content, 'html.parser')

      nuevaurl=soup.find("a",class_="link")['href']

      Lmunicipios["muni"].append({

        "ccaa":prtpob,
        "nombre":pov,
        "enlace":nuevaurl

      })

      cont=+1





  return Lmunicipios








def listapoblacpocas(comm):
  pagina = requests.get(comm)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  enlaces=[]
  i=1
  nombres=[]


  for poblacion in soup.find_all("div", class_="baseCard riverCard locationCard gridCardlargeCard"):

    enlaces.append(poblacion.find("a",class_="titleItem")['href'])
    prtpob=poblacion.find("a",class_="titleItem").getText()
    print(i , prtpob)
    nombres.append(prtpob)
    i=i+1



  return enlaces,nombres



def listapoblaciones(url):
  pagina = requests.get(url)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  enlaces=[]
  i=1
  nombres=[]
  

  for poblacion in soup.find_all("div", class_="baseCard riverCard locationCard gridCard"):

    enlaces.append(poblacion.find("a",class_="titleItem")['href'])
    prtpob=poblacion.find("a",class_="titleItem").getText()


    nombres.append(prtpob)
    print(i , prtpob)
    i=i+1



  return enlaces,nombres







def mostrarcosas(url):

  pagina = requests.get(url)
  soup = BeautifulSoup(pagina.content, 'html.parser')

  nuevaurl=soup.find("a",class_="link")['href']

  pagina = requests.get(nuevaurl)
  soup2 = BeautifulSoup(pagina.content, 'html.parser')



  for link in soup2.find_all("a",class_="link"):
    print(link.get("href"))
    pagina3 = requests.get(link.get("href"))
    soup3 = BeautifulSoup(pagina3.content, 'html.parser')

    for element in soup3.find_all("a", class_="titleItem"):

      prtpob=element.getText()
      print(prtpob)

    linkcomp = soup2.findAll("a", class_="next button")

    siguiente=linkcomp[0].get("href")

    if type(siguiente) == None :
      siguiente="out"

  linkcomp = soup2.findAll("a", class_="next button")
  if len(linkcomp) != 0 :
    siguiente=linkcomp[0].get("href")
  else:
    siguiente="out"

  while(siguiente!="out"):


    #itemsGrid

    pagina2 = requests.get(siguiente)
    soup2 = BeautifulSoup(pagina2.content, 'html.parser')

    for element in soup2.find_all("a",class_="titleItem"):

     print(element.getText())

    linkcomp = soup2.findAll("a", class_="next button")
    if len(linkcomp) != 0 :
      siguiente=linkcomp[0].get("href")
    else:
      siguiente="out"
















