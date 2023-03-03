from bs4 import *
import requests


def municipiosprinci():
  # Link
  r = requests.get(f'https://15mpedia.org/w/index.php?title=Especial:Ask&offset=0&limit=8131&q=%5B%5BPage+has+default+form%3A%3AMunicipio%5D%5D+%5B%5Bpa%C3%ADs%3A%3AEspa%C3%B1a%5D%5D&p=format%3Dtable%2Fmainlabel%3DMunicipio&po=%3F%3DMunicipio%23%0A%3FComarca%23-%0A%3FProvincia%0A%3FComunidad+aut%C3%B3noma%3DCC.AA.%0A%3FAltitud%3DAltitud+%28m.s.n.m.%29%0A%3FSuperficie%3DSuperficie+%28km%C2%B2%29%0A%3FPoblaci%C3%B3n+en+2019%3DPoblaci%C3%B3n+%282019%29%0A%3FDensidad+de+poblaci%C3%B3n%3DDensidad+%28hab.%2Fkm%C2%B2%29%0A&sort=nombre&order=asc')
  municipios={}
  municipios['municipio']=[]


  # Procesar texto y etiquetas html
  content = r.text
  soup = BeautifulSoup(content, 'html.parser')
  table = soup.find('tbody')
  rows = table.find_all('tr')
  i = 0

  # Bucle que recorre las filas de la tabla
  for row in rows:
    municipio={}
    i = i +1
    municipio['name'] = row.find('td', {"class": "Municipio"}).text.replace("'"," ")
    
    # Para poner nombre del municipio
    logo = row.find('td', {"class": "Municipio"})

    # Para buscar la etiqueta a dentro del 'td'
    link_ = logo.find('a')
    
    # URL personalizada para todos los links de municipios
    r = requests.get('https://15mpedia.org' + link_['href'])
    
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    
    # Si no hay imagen
    if soup.find('a', {"class": "image"}) is None:
      municipio['image'] = 'NULL'
    else: # Obtenemos la imagen asociada al municipio
      image = soup.find('a', {"class": "image"})
      link = requests.get('https://15mpedia.org' + image['href'])
      content = link.text
      soup = BeautifulSoup(content, 'html.parser')
      
      # Lo mismo que arriba pero con la imagen a mejor resolucion
      if soup.find('div', {"class": "fullImageLink"}) is None:
        municipio['image'] = 'NULL'
      else:
        fullImage = soup.find('div', {"class": "fullImageLink"})
        svgImage = fullImage.find('a')
        municipio['image'] = svgImage['href']
    
    # Comarca
    if row.find('td', {"class": "Comarca"}) is None:
      municipio['region'] = ''
    else:
      municipio['region'] = row.find('td', {"class": "Comarca"}).text.replace("'"," ")
    
    # Provincia y comunidad autonoma
    municipio['province'] = row.find('td', {"class": "Provincia"}).text.replace("'"," ")
    municipio['aacc'] = row.find('td', {"class": "CC.AA."}).text.replace("'"," ")
    
    # Si no tiene poblacion
    if row.find('td', {"class": "Población-(2019)"}) is None:
      municipio['population'] = str(0)
    else:
      municipio['population'] = row.find('td', {"class": "Población-(2019)"}).text.replace('.','')
      
    # Si no tiene densidad
    if row.find('td', {"class": "Densidad-(hab./km²)"}) is None:
      municipio['density'] = str(0)
    else:
      municipio['density'] = row.find('td', {"class": "Densidad-(hab./km²)"}).text.replace( '.','').replace(',','.')
    
    # Municipios scrappeados
    #print('municipio ' + str(i) + ' scrappeado correctamente')

    municipios['municipio'].append({
      'nombre':municipio['name'],
      'image':municipio['image'],
      'region':municipio['region'],
      'province':municipio['province'],
      'aacc':municipio['aacc'],
      'population':municipio['population'],
      'density':municipio['density']
    })
    print("agregando a la lista ",municipio["name"])



    



  return municipios