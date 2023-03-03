import { Component, OnInit, AfterViewChecked } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-nuevo-user',
  templateUrl: './nuevo-user.component.html',
  styleUrls: ['./nuevo-user.component.scss'],
  providers: [ApiService]
})
export class NuevoUserComponent implements OnInit, AfterViewChecked {

  nombre:any=""
  password:any=""
  tok:string=""
  errorMessage: boolean = false
  constructor(private http: HttpClient,private activatedRoute:ActivatedRoute, private router:Router, private api: ApiService) { }
  ngAfterViewChecked(): void {
    
  }

  ngOnInit(): void {


  }
  btnAddUser(nombre:string, password:string) {
    var nombreUsuario = JSON.parse(JSON.stringify(nombre))
    var passwordUsuario = JSON.parse(JSON.stringify(password))
    console.log('recojo', nombreUsuario, passwordUsuario)
    this.tok=localStorage.getItem("token")!
    this.api.addUsuario(nombre, password,this.tok).subscribe((res) =>
    {
      this.nombre = res.nombre
      this.password = res.password
      console.log('Usuario Registrado!!!!!');

    },error=>this.createError());

  }
  createError(){
    this.errorMessage=true
  }
}
