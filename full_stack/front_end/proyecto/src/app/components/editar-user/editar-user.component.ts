import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';

import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-editar-user',
  templateUrl: './editar-user.component.html',
  styleUrls: ['./editar-user.component.scss'],
  providers: [ApiService]
})
export class EditarUserComponent implements OnInit {
  datosU:Array<any>=[]
  id:string=""
  nombre:string=""
  tok:any=""

  constructor(private http: HttpClient,private activerouter:ActivatedRoute, private router:Router, private api: ApiService) { }

  ngOnInit(): void {


    //console.log(sessionStorage.getItem("idEditar"));

    this.activerouter.queryParams.subscribe((data=>{
      this.id = data["id"]
    }));


    //this.id=sessionStorage.getItem("idEditar")

    console.log(this.id)

    this.api.getSingleUser(this.id).subscribe((res) =>
    {
      console.log('Res ', res.usuario);
      this.datosU = res.usuario;
      this.nombre = res.usuario["nombre"];

    });

  }

  btnEliminar() {
    this.api.deleteUsuario(this.id).subscribe((res) =>
    {
      console.log('Usuario ELIMINADO!!!!');
      this.router.navigate(['users'])
    });
  }

  btnAceptar(nombre:string) {
    var nombreUsuario = JSON.parse(JSON.stringify(nombre))
    console.log('recojo', nombreUsuario)

   

    this.api.editarUsuario(this.id,nombre).subscribe((res) =>
    {
      this.nombre = res.nombre
      console.log('Usuario Editado!!!!!');
      this.router.navigate(['users'])
      
    });  
  }
}
