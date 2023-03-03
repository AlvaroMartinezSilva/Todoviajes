from django.db import models

# Create your models here.


class Usuario(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=100)
    tipoUS=models.CharField(max_length=30)

    class Meta:
        db_table = "Usuario"

class Municipio(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField(max_length=60)
    ccaa=models.CharField(max_length=30)
    enlace=models.CharField(max_length=1000)
    contador=models.IntegerField()

    class Meta:
        db_table = "Municipio"
     
class Quever(models.Model):
    id = models.AutoField(primary_key=True)
    idMunicipio=models.ForeignKey(Municipio,null=True,on_delete=models.CASCADE) ## si se elimina, se elimina el resto de relaciones
    direccion=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    contacto=models.CharField(max_length=30)
    foto=models.TextField()

    class Meta:
        db_table = "Quever"

class Config(models.Model):
    id= models.AutoField(primary_key=True, serialize=False, unique=True)
    opcion=models.CharField(max_length=30)
    valor=models.CharField(max_length=30)

    class Meta:
        db_table = "Config"

class Busqueda(models.Model):
    id= models.AutoField(primary_key=True, serialize=False, unique=True)
    idMunicipio=models.ForeignKey(Municipio,null=True,on_delete=models.CASCADE) ## si se elimina, se elimina el resto de relaciones
    odio=models.FloatField(default=0)
    odioNoticias=models.FloatField(default=0)
    odioComentarios=models.FloatField(default=0)
    Actualizar=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "Busqueda"
    