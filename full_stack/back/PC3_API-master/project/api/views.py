


from django.http import JsonResponse
from datetime import datetime,timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Busqueda, Municipio, Usuario,Config,Quever
import json

import llamar


from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator





import ElMundo,elPais,Minutos,Tablacrearmuni
import minube
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.views import ObtainAuthToken
from datetime import datetime,timezone,timedelta
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password




class UsuariotView(APIView): 
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):           ## para evitar el csrf
        return super().dispatch(request, *args, **kwargs)


    @csrf_exempt
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def post(request): ##necesita parametros pero no en la url
     
        #authentication_classes = ()
        print("1")
        #usuarios=list(Usuario.objects.values()) ##convertirlo a lista para que se peuda pasar en json en el JSONresponse
        #print(request.body) ##para imprimir en esta consola resultados
        jsonData=json.loads(request.body)  ## transformar lo que venga del json a un diccionario entendible para python
        #print(jsonData)
        print("2")
        if(jsonData['nombre']!=""):
            HashedPassword=make_password(password=jsonData['password'],salt="MeEncantaPC3")
            print("3")
            Usuario.objects.create(nombre=jsonData['nombre'],password=HashedPassword,tipoUS="Admin") ## jsonData['tipoUS']
            print("4")
            datos={'message':["success"]}
            print("5")

            return JsonResponse(datos)
        else:
            raise AuthenticationFailed('Nombre requerido')

    @api_view(['PUT'])
    @permission_classes([IsAuthenticated])
    def put(request,id): ##actualizar por id / http://127.0.0.1:8000/Usuarios/get/1 UTILIZAR PARAMETROS (PUT)
        jsonData=json.loads(request.body)
        id=jsonData['id']
        usuario=list(Usuario.objects.filter(id=jsonData['id']).values())    ## filtrar por id para validar que existen antes de actualizar
        if len(usuario)>0:
                usuario=Usuario.objects.get(id=id)
                usuario.nombre=jsonData['nombre']
                if('contrasenia' in jsonData):               ##como ya vi que existe, hacer get
                    HashedPassword=make_password(password=jsonData['contrasenia'])
                    usuario.password=HashedPassword
                if('tipoUS' in jsonData): 
                    usuario.tipoUS=jsonData['tipoUS']
                usuario.save()                                  ## para guardar los cambios
                datos={'message':"success"}
        else:
                datos={'message':"no se encontraron usuarios"}
        return JsonResponse(datos)

    @api_view(['DELETE'])
    @permission_classes([IsAuthenticated])
    def delete(request,id):  ##  http://127.0.0.1:8000/Usuarios/get/2
        usuario=list(Usuario.objects.filter(id=id).values())    ## filtrar por id para eliminar
        if len(usuario)>0:
            Usuario.objects.filter(id=id).delete()
            datos={'message':"success"}
        else:
            datos={'message':"no se encontraron usuarios"}
        return JsonResponse(datos)


   
## Con esta funcion borro las COOKIES y se cierra la sesion del USUARIO

#############################################################  CLASE LOGOUT  ############################################################# 


## Con esta funcion se hace el logueo(validacion del usuario) y se crea el JWT token

#############################################################  CLASE LOGIN  ############################################################# 
class LoginView(ObtainAuthToken):

    ##login
    ## andres - 123
    ## prueba2 - 1234

    @api_view(['POST'])
    def login(request):
        ## Creacion de varoables para el request y el response
        jsonData={}
        datos={}
        jsonData=json.loads(request.body)
        
        ## Credenciales mandadas en el REQUEST
        contraREQ=jsonData['contrasenia']
        userREQ=jsonData['username']
        print("contrasenia REQ: "+contraREQ)
        print("usuario REQ: "+userREQ)
        
        ## Obtener usuario de BD con el user del REQUEST
        try:
            usuarios=Usuario.objects.get(nombre=jsonData["username"])
        except Usuario.DoesNotExist:
            usuarios = None
        ## Validar que exista usuario
        
        if usuarios is None:
            #datos={"message":"usuario no existe"}
            #return JsonResponse(datos)
            raise AuthenticationFailed('usuario o contraseña incorrectos')
        else:   
        ## Credenciales obtenidas de la BD con el usuario
            contraBD=usuarios.password
            userDB=usuarios.nombre
            idDB=usuarios.id
            print("contrasenia DB: "+contraBD)
            print("user DB:  "+userDB)
            #contraREQhash=make_password(password=contraREQ)
            #print("contrasenia: "+contraREQhash )
            print("LA CONTRASENIA DE REQ HASSHEADA ES: "+ make_password(password=contraREQ))
            print("LA CONTRASENIA DE DB: "+ contraBD)
            print("LA CONTRASENIA ES: "+ str(check_password(contraREQ,contraBD)))
            if userREQ==userDB and check_password(contraREQ,contraBD)==True:
                #datos={"message":"inicio exitoso","token":""}
                payload={
                    'id':idDB,
                    'rol':'admin',
                    'exp':datetime.now()+timedelta(minutes=60), ## token valido por 60 minutos
                    'iat':datetime.now()                                 ## fecha en la que se crea el token
                }
                token=jwt.encode(payload,'secret',algorithm='HS256')
                
                response=Response()    
                response.set_cookie(key='jwt',value=token,httponly=True)
                refresh = RefreshToken.for_user(usuarios)
                response.data={
                    'jwt':str(refresh.access_token)
                }
                
                ## probar funcion ##
                #tokenNuevo= getUserTokens(usuarios)
                #response1=Response()    
                #response1={"prueba token":tokenNuevo}
                #return response1
                ## probar funcion ##
                return response
                
                #datos={"message":"inicio exitoso","token":token}
            else:
                #datos={"message":"usuario o contrasenia invalidos","token":""}
                raise AuthenticationFailed('Usuario o contraseña incorrectos')
    



    
#############################################################  SCRAPER  #############################################################

## peticion GET Scraper

@api_view(['GET'])
def busqueda(request):
    
    analisis=0
    nombreMunicipio=request.GET.get('id')

   
    print(nombreMunicipio)
    activar=False

    
    municipio=Municipio.objects.get(nombre=nombreMunicipio)

    
    munId=municipio.id
    
    z=municipio.contador
    print(type(z),z)
    z=z+1
    municipio.contador=z

    municipio.save()



    fecha=datetime.now(timezone.utc) 



    fActual =datetime.now(timezone.utc) 

   

  

    difer=3
    difer=Config.objects.get(opcion="dias")
    





    dif=(fActual-fecha).days


    try:
        compAct=Busqueda.objects.get(idMunicipio=munId)
        
        fecha:datetime= compAct.Actualizar
    except:
       
        activar=True


    if(dif>int(difer.valor)): 
        activar=True
  




    if(activar):

        mediaSentNoticias=0
        fActual = datetime.strftime(fActual,"%d-%m-%Y %H:%M:%S")
        #Scrapers de noticias 
        mundoTxt=ElMundo.principalelMund(nombreMunicipio)
        contador=0
        sentA=0
        print("analizando texto")   
        for text in mundoTxt:
            sentA=llamar.sent(text)+sentA
            contador+=1
        if(contador!=0):
            sentA=sentA/contador
        else:
            sentA=0
        minutosTxt=Minutos.principal20mins(nombreMunicipio)
        contador=0
        sentB=0
        print("analizando texto")
        for text in minutosTxt:
            sentB=llamar.sent(text)+sentB
            contador+=1
        
        if(contador!=0):
            sentB=sentA/contador
        else:
            sentB=0
        paisTxt=elPais.principalelPais(nombreMunicipio)
        contador=0
        sentC=0
        print("analizando texto")
        for text in paisTxt:
            sentC=llamar.sent(text)+sentC
            contador+=1
        if(contador!=0):
            sentC=sentA/contador
        else:
            sentC=0
        
        mediaSentNoticias=(sentA+sentB+sentC)/3
      
       
        minubels=minube.principalmibe(municipio.enlace)
        sumasent=0
        contador=0
        opiniones=""
        #for mbel in minubels['QueVer']:
        for mbel in minubels:
           

            qver = Quever.objects.filter(nombre=mbel["nombre"]).exists()
            print(qver)
            print(mbel["nombre"])
            if(qver==False):

                print("agregando")
                Quever.objects.create(nombre=mbel["nombre"],direccion=mbel['direccion'],contacto=mbel['Contacto'],foto=mbel['Foto'],idMunicipio=municipio) ##extraer parametros para extraerlos
                

            for op in mbel['Opinion']:
                opiniones=opiniones+op
                
        sumasent=llamar.sent(op)+sumasent
        contador+=1

            
        if (contador!=0):
            mediaSentComentarios=sumasent/contador
        else:
            mediaSentComentarios=0

        mediaSentTotal = (mediaSentNoticias + mediaSentComentarios)/2

        

        Busqueda.objects.create(odio=mediaSentTotal,odioNoticias=mediaSentNoticias,odioComentarios=mediaSentComentarios,Actualizar=fActual,idMunicipio=municipio)
    

    



    ############ ------------------------- ############ 
    ## minube devuelve un array de json minube (nombremunicipio)###

    ############  deolver odios de municpio y lista de quevers  ############
    
    #municipios1=list(Municipio.objects.filter(nombre=nombreMunicipio).values())
    
    municipios1=Municipio.objects.get(nombre=nombreMunicipio)

    compAct=Busqueda.objects.filter(idMunicipio=munId)
    arg = compAct.order_by('-Actualizar')[0]

    municipios1.save()

    
    Odio=arg.odio
    OdioNoticias=arg.odioNoticias
    OdioComment=arg.odioComentarios

    datos={}
    datos=[]
    
    #lsquevermin=[]
    #lsquevermin["data"]=[]
    #qv=obtenerQuevers(munId)
    
    #for qu in qv:

    #    lsquevermin["data"].append({

    #            "id":qu.id,
    #            'Foto': qu.foto,
    #            'nombre': qu.nombre,
             
    #    })

    datosfinales=obtenerQuevers(munId)
    listaFinal={"NombreMunicipio":nombreMunicipio,"Odio":Odio,"OdioNoticias":OdioNoticias,"OdioComment":OdioComment,"Quevers":datosfinales}
    
    return JsonResponse(listaFinal)




def obtenerQuevers(MunicipioId):
    #nombreMunicipio=request.GET.get('id')

    quevers=list(Quever.objects.filter(idMunicipio=MunicipioId).values())
    if(len(quevers)>0):

        datos=quevers
        
    else:
        datos={"municipio":"municipio no encontrado"}
    
    return datos



@api_view(['POST'])
def municipioscrear(request):

    
    # x=municipios.municipiosprinci()

    
    # for mun in x['municipio']:

        
    #     strnom=mun['nombre']
    #     strccaa=mun["aacc"]
    #     print("agregando a la base de datos ",strnom)  
    #     x=Municipio.objects.create(nombre=strnom,contador=0,ccaa=strccaa)
        
    #     x.save()

    funcion=Tablacrearmuni

    minibuffer=funcion.comunidadesmenu()
    
    for mun in minibuffer["muni"]:

        Municipio.objects.create(nombre=mun["nombre"],ccaa=mun["ccaa"],enlace=mun["enlace"],contador=0)




   
        

    datos={'message':"tablacreada"}
    


    return JsonResponse(datos)

@api_view(['GET'])
def ObtenerQueverDetallado(request):
    idQuever=request.GET.get('id')
    quevers=list(Quever.objects.filter(id=idQuever).values())
    if(len(quevers)>0):
        queverFinal=quevers
        datos={"Quever":queverFinal}
    else:
        datos={"Message":"Que ver no encontrado"}
    
    return JsonResponse(datos)
 
        
@api_view(['GET'])
def obtenerMunicipios2(request):
    municipios=list(Municipio.objects.values())
    if(len(municipios)>0):
        municipio=municipios
        datos={"municipio":municipio}
    else:
        datos={"municipio":"municipio no encontrado"}
    
    return JsonResponse(datos)


@api_view(['GET'])
def datosgrafica(request):
    
    datos=list(Municipio.objects.order_by('-contador')[:10])
    
    
    usuariosdata={}

    usuariosdata["data"]=[]

   

    for nom in datos:
        usuariosdata["data"].append(
            {
                "id":nom.nombre,
                "count":nom.contador
             

            }
        )
    
    return JsonResponse(usuariosdata)



@api_view(['GET'])
def datosmostrarmasbusc(request):

    datos=list(Municipio.objects.order_by('-contador')[:3])

    usuariosdata={}

    usuariosdata["data"]=[]

   

    for nom in datos:
        usuariosdata["data"].append(
            {
                "id":nom.nombre
             
            }
        )
    
    return JsonResponse(usuariosdata)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getListaUsuarios(request):

    datos = list(Usuario.objects.values())

    usuariosdata={}

    usuariosdata["data"]=[]

    m=Usuario.objects.all()

    for nom in m:
        usuariosdata["data"].append(
            {
                "id":nom.id,
                "nombre":nom.nombre,
                "tipoUS":nom.tipoUS
            }
        )
    
    return JsonResponse(usuariosdata)

@api_view(['POST'])
def idUsuario(request):
    id=request.data["id"]

    print("*****",id)
    
    usuarios=list(Usuario.objects.filter(id=id).values())
    if len(usuarios)>0:
        usuario=usuarios[0]         ##agarro el match del id para ponerlo en el resultado
        datos={'usuario':usuario}
    else:
        datos={'usuario':"no se encontraron usuarios"}
    return JsonResponse(datos)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def actopcion(request):

    tiempo=request.data["valor"]
    print("cambiado")
    opt=Config.objects.get(opcion="dias")
    opt.valor=tiempo
    opt.save()

    return JsonResponse({"val":"cambiado"})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUsuario(request,id):  ##  http://127.0.0.1:8000/Usuarios/get/2
    usuario=list(Usuario.objects.filter(id=id).values())    ## filtrar por id para eliminar
    if len(usuario)>0:
        Usuario.objects.filter(id=id).delete()
        datos={'message':"success"}
    else:
        datos={'message':"no se encontraron usuarios"}
    return JsonResponse(datos)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUsuario(request): ##necesita parametros pero no en la url
    #nombre=request.data["nombre"]
    #password=request.data["password"]
    authentication_classes = ()
    #usuarios=list(Usuario.objects.values()) ##convertirlo a lista para que se peuda pasar en json en el JSONresponse
    #print(request.body) ##para imprimir en esta consola resultados
    jsonData=json.loads(request.body)  ## transformar lo que venga del json a un diccionario entendible para python
    #print(jsonData)
    HashedPassword=make_password(password=jsonData['password'],salt="MeEncantaPC3")
    Usuario.objects.create(nombre=jsonData['nombre'],password=HashedPassword,tipoUS="Admin") ## jsonData['tipoUS']
    datos={'message':["success"]}

    return JsonResponse(datos)
