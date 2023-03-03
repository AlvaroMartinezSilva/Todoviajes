from django import views
from django.urls import path
from requests import post
#from .views import UsuarioListView, fexternal ##importar la vista
#from .views import UsuarioPostView ##importar la vista
#from .views import button ##importar la funcion del script
#from .views import output
#from .views import fexternal #, get,getById
from .views import UsuariotView
from .views import busqueda
from .views import municipioscrear #,get
from .views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
# urls para administrar usuarios


path('usuarios/post/', UsuariotView.post), ## registrar
path('usuarios/put/<int:id>/', UsuariotView.put), ## obtener un usuario por su id

path('listaUsuarios', getListaUsuarios), ##Lista completa de usuarios
path("idUsuario/",idUsuario),
path("deleteUsuario/delete/<int:id>",deleteUsuario),
path("addUsuario",addUsuario),



# login
path('login/',LoginView.login),

#busquedas de municipas hechas por usuarios
path('busqueda/',busqueda),

#BUSCA, ENCUENTRA Y GUARDA 8000 MUNICIPIOS ---- NO USAR
path("crear/",municipioscrear),






# Obtener los detalles de cada quever
path("queverdetalle/",ObtenerQueverDetallado),

# Obtener la lista de municipios
path("listmunicipios/",obtenerMunicipios2),

# obtener el numero de visitas (contador) por municipio pero en 10 visitas
path('datosgrafica/',datosgrafica),

# obtener el numero de visitas (contador) por municipio pero en 3 visitas
path('datosmostrarmasbusc/',datosmostrarmasbusc),

# Modificar el numero de dias en tabla config
path('actopcion/',actopcion)


]

