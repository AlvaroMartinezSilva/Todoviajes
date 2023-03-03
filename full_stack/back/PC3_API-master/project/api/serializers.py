from rest_framework import serializers
#from .models import Municipio, Usuario 
from .models import Usuario 

class UsuarioSerializer(serializers.ModelSerializer): ## necesitamos serialziarlo para convertirlo en un json
    class Meta:
        model = Usuario
        fields='__all__'

#class MunicipioSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Municipio
#        fields=('municipiosFav')
