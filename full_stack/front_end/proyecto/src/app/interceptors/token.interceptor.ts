import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpHeaders,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {

  constructor() {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    if(localStorage.getItem('token')!=null){
    console.log('AL', 'interceptor')
    //obetener el token
    var token = 'Bearer '+localStorage.getItem('token')

    //crear los headers
    const headers = new HttpHeaders({
      'Authorization': token
    });

    //clonar la request para modificarla con los headers
    const requestClone = request.clone({
      headers
    });

    return next.handle(requestClone).pipe(
      catchError(this.manejarError)
    );}else{
      console.log('al', 'interceptor')
      //obetener el token
      var token = 'bearer '+localStorage.getItem('token')

      //crear los headers
      const headers = new HttpHeaders({
        'Authorization': token
      });

      //clonar la request para modificarla con los headers
      const requestClone = request.clone({
        headers
      });

      return next.handle(requestClone).pipe(
        catchError(this.manejarError)
      );

    }
  }

  manejarError(error : HttpErrorResponse){
    console.log(console.error)
    //return throwError(() => new Error('Fallo en la petición rest'))
    return throwError(error)
  }
}
