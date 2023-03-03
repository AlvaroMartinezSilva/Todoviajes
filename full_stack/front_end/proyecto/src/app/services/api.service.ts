  import { Injectable } from '@angular/core';
  import { Observable } from 'rxjs';
  import { environment } from 'src/environments/environment';
  import { HttpClient, HttpHeaders } from '@angular/common/http';


  @Injectable({
    providedIn: 'root'
  })

  export class ApiService {

    constructor(private http: HttpClient) { }

    mandarMunicipio(nombreMunicipio: string): Observable<any> {

      var respuestaAPI = this.http.get<any>(environment.api + 'busqueda/?id=' + nombreMunicipio);

      return respuestaAPI;
    }

    obtenerMunicipios(): Observable<any> {

      var respuestaAPI = this.http.get<any>(environment.api + 'listmunicipios/');

      return respuestaAPI;
    }

    obtenerQueVerVistaLocal(idQueVer: number): Observable<any> {

      var respuestaAPI = this.http.get<any>(environment.api + 'queverdetalle/?id=' + idQueVer);

      return respuestaAPI;
    }

    pedirToken(usuario:string, contrasenia:string): Observable<any> {

      let cuerpo = {
        'username': usuario,
        'contrasenia': contrasenia
      }
      var respuestaAPI:any = this.http.post<any>(environment.api+'login/', cuerpo);

      return respuestaAPI
    }

    borrarToken() {

      localStorage.removeItem('token')

    }

    isLogin() :boolean{
      var tieneToken = false
      if(localStorage.getItem('token')){
        tieneToken = true
      }else{
        tieneToken = false
      }
      return tieneToken
    }





    getUsers():Observable<any> {

      var respuestaAPI:any = this.http.get<any>(environment.api+'listaUsuarios');

      return respuestaAPI
  }

  getSingleUser(id:string):Observable<any>{

    var req={"id":id}

    let respuestaAPI = this.http.post<any>(environment.api + 'idUsuario/',req);
    return respuestaAPI
  }

  deleteUsuario(id:string):Observable<any>{

    //var req={"id":id}
    let respuestaAPI = this.http.delete<any>(environment.api + 'deleteUsuario/delete/'+id);
    return respuestaAPI
  }

  addUsuario(nombre:string, password:string,tok:string):Observable<any>{

    var req={"nombre":nombre,
            "password":password}



    let respuestaAPI = this.http.post<any>(environment.api + 'usuarios/post/',req);
    return respuestaAPI
  }

  editarUsuario(id:string, nombre:string):Observable<any> {

    var req ={
      "id":id,
      "nombre":nombre,
    }

    let respuestaAPI = this.http.put<any>(environment.api + 'usuarios/put/'+id+'/',req);
    return respuestaAPI
  }


  datosgrafica():Observable<any>{

    let respuestaAPI = this.http.get<any>(environment.api + 'datosgrafica/');
    return respuestaAPI

  }

  datosmostrarmasbusc():Observable<any>{

    let respuestaAPI = this.http.get<any>(environment.api + 'datosmostrarmasbusc/');
    return respuestaAPI

  }


  actopcion(value:string):Observable<any>{

    var req={"valor":value}
    let respuestaAPI = this.http.post<any>(environment.api + 'actopcion/',req);

    return respuestaAPI
  }


  }
