import json
from pickle import FALSE, TRUE
import requests
from bs4 import BeautifulSoup
import pandas as pd

def principalmibe(enlace):

            
        
    print(enlace)


    data={}
    data['QueVer']=[]
    siguiente=" "

    while(siguiente!="out"):

        print(enlace)
        pagina = requests.get(enlace)
        soup = BeautifulSoup(pagina.content, 'html.parser')
        rows = soup.select(".itemsGrid a.titleItem")
        

        for row in rows:

            linkdatos=row.get('href')
            redatos = requests.get(linkdatos)
            soupdatos = BeautifulSoup(redatos.content, 'html.parser')

            #Obtencion de datos
            datosLugar = soupdatos.find_all("a", {"class": "data"})
            imagen = soupdatos.find("img", {"class": "picture"})
            opinion = soupdatos.find_all("div", {"class": "textContainer"})
            nombresitio=soupdatos.find_all("h1")
            #URL siguiente, para paginacion

                

            if nombresitio == None:
                #print("Sin imagenes")
                nombresitio="sin nombre"
                
            else:
                nombresitio = soupdatos.find("h1").getText()
                #print(imagen)
                #print("1---------------" + "\n")

            if imagen == None:
                imagen=("Sin imagenes")
                
                
            else:
                imagen = soupdatos.find("img", {"class": "picture"}).get('data-src')
                #print(imagen)
                #print("1---------------" + "\n")

            if datosLugar == None:
                ##print("Sin dirección")
                datosLugar=" "
                
            else:
                datosLugar = soupdatos.find_all("a", {"class": "data"})
                listaLugar = []
                for element in datosLugar:
                    a = element.get_text()
                    listaLugar.append(a)
                    #print(a)
                
                #print("2---------------" + "\n")

            if opinion == None:
                #print("Sin opinión")
                opinion(" ")
                
            else:
                opinion = soupdatos.find_all("div", {"class": "textContainer"})
                listaOp = []
                for element in opinion:
                    a = element.get_text()
                    listaOp.append(a)
                    #print(a)
                
                #print("3---------------" + "\n")
            
            data['QueVer'].append({
                'direccion': linkdatos,
                "nombre":nombresitio,
                'Foto': imagen,
                'Contacto': listaLugar,
                'Opinion': listaOp
            
                })
            print("Agregando a lista ",nombresitio)


        print(linkdatos)


        linkcomp = soup.findAll("a", class_="next button")

        

        if (len(linkcomp) < 1) :
            siguiente="out"
        else:
            siguiente=linkcomp[0].get("href")
            linkcomp = soup.findAll("a", class_="next button")

            if len(linkcomp) != 0 :
                enlace=linkcomp[0].get("href")
                siguiente=" "
            else:
                siguiente="out"


        print(siguiente)




    return data['QueVer']












    # r = requests.get(enlace)
    # soup = BeautifulSoup(r.content, 'html.parser')
    # pagina = soup.find_all("div", {"class": "display_table buttonMain"})

    # ultPag = pagina.pop(1)
    # paginaFinal = int(ultPag.get_text())
    # print(paginaFinal)
    # #Linea necesaria para reducir el tiempo de desarrollo BORRAR DESPUES
    # #paginaFinal = 2

    #Paginacion para la web
   


        

        # ##print(pag)
        # url = str(var) +'?page='+ str(pag)
        # print(url)
        # req = requests.get(url)
        
        # soup3 = BeautifulSoup(req.content, 'html.parser')

        # # Alternativa a find_all o find
        # rows = soup.select(".itemsGrid a.titleItem")

        #for row in rows:

            # link = row.get('href')
            # ##print("Link de la web: " + link + "\n")

            # #Ingreso en cada URL
           

  
            
            #thisdict = {"direccion": link, "Foto": imagen, "Contacto": listaLugar,"Opinion": listaOp,"idMunicipio_id":nombre}


    

# rows = soup.find_all("div", {"class": "riverItems"})
# rows = soup.find_all("a", {"class": "titleItem"})

# print(rows)


