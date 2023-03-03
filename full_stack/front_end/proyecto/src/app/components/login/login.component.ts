import { HttpClient } from '@angular/common/http';
import { ChangeDetectionStrategy, Component, OnInit, AfterViewChecked } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { NavbarComponent } from '../navbar/navbar.component';
import { NgModel } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers: [ApiService]
})
export class LoginComponent implements OnInit, AfterViewChecked {

  usuario=''
  contrasenia=''
  errorMessage: boolean = false

  constructor(private router: Router, private http: HttpClient, private api: ApiService) { }
  ngAfterViewChecked(): void {

  }

  ngOnInit(): void {
  }

  logIn(): void{
    this.api.pedirToken(this.usuario, this.contrasenia).subscribe((res) =>
    {
      var token;
      try{
        token=res.jwt
        localStorage.setItem('token', token)
        this.router.navigate(['/admin'])
      }catch{
        token='Fallo en el login'

        console.log(token)
      }
    },error=>this.logInError());
  }

  logInError(){
    this.errorMessage=true
    this.revisarLogin()
  }

  revisarLogin():boolean{
    var hayError = false
    if(this.errorMessage){
      hayError=true
    }else{
      hayError=false
    }
    return hayError
  }

}
