# PC3_API
AVANCE DE API ENTREGA 28 ABRIL
## Instrucciones para comprobar que se ejecuta el script con POSTMAN

1.Abrir el proyecto 
<br/>
<br/>
2.Ubicarse dentro de la carpeta del proyecto
<br/>
<br/>
3. Si no se tiene, se debe instalar django: pip install django
4. Si no se tiene, se debe instalar rest_framework: pip3 install djangorestframework
5. Si no se tiene, se debe instalar rest_framework_simplejwt: pip install djangorestframework-simplejwt
6. Si no se tiene, se debe instalar django_cors_headers: pip install django-cors-headers
7. Sii no se tiene, se debe instalar pymysql: pip install pymysql
8. Iniciar el servidor: python ./manage runserver
<br/>
<br/>
9. Ir a POSTMAN y hacer el request como se ve en la imagen. El parametro siempre debe ser "id" y el valor en este caso 1.
<br/>
![image](https://user-images.githubusercontent.com/52229171/165817433-beee692f-3db4-4b5e-a654-de23d07532ad.png)
<br/>
<br/>
10. Lo que se hizo aquí es importar el archivo del web scraper/analizador de sentimientos al proyecto y llamarlo con la API a traves de una URL para analizar el sentimiento de una noticia elegida especificamente para esta prueba. Con esto se devuelve un emoji de carita feliz, triste o neutro y el score del sentimiento en formato json.
<br/>
<br/>
11.Las migraciones están en la carpeta de migraciones y tambien se ha creado el archivo db.sqlite3. En la imagen de abajo está nuestro diagrama Entidad-Relación.
<br/>
![image](https://user-images.githubusercontent.com/52229171/165841642-6981effd-1596-40e6-a9ec-f9ec10f8d79d.png)
