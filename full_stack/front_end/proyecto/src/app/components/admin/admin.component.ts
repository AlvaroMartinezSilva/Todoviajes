import { HttpClient } from '@angular/common/http';
import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import * as Highcharts from 'highcharts';
import { ApiService } from 'src/app/services/api.service';
import { TarjetaComponent } from '../tarjeta/tarjeta.component';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss'],
  providers: [ApiService]
})
export class AdminComponent implements OnInit {

  busqueda:Array<any>=[]


  constructor(private router:Router, private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService) { }

  @Input() update:number = 1;
  sideBarOpen = true;
  lista:string[]=["3","5","7", "10"];
  seleccionado:string="";

  ngOnInit(): void {
    this.api.datosmostrarmasbusc().subscribe((res) =>
    {
      console.log('Res ', res.data);
      this.busqueda = res.data
    });
  }
  sideBarToggler() {
    this.sideBarOpen = !this.sideBarOpen;
  }

  //Metodo para actualizar datos de la BBDD desde la pantalla admin
  cambio(obj:string){

  this.seleccionado=obj
  console.log(this.seleccionado)
  this.api.actopcion(this.seleccionado).subscribe(() =>{

    console.log("nope")

  });

  }
}


