import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss'],
  providers: [ApiService]
})
export class UsersComponent implements OnInit {


  constructor(private http: HttpClient,private api: ApiService, private router: Router) { }

  datosU:Array<any>=[]

  ngOnInit(): void {
    console.log("**********************")
    this.api.getUsers().subscribe((res) =>
    {
      console.log('Res ', res.data);
      this.datosU = res.data;
    });
  }


  editarUsuario(id:number) {

    let guard=id.toString()
    //sessionStorage.setItem("idEditar", guard )

    this.router.navigate(['editar'],{queryParams:{"id":guard}})
    console.log(guard);

  }
    nuevoUser() {
      this.router.navigate(['crear'])
    }
}
