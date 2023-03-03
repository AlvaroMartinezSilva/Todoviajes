import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { ActivatedRoute } from '@angular/router';
import { TarjetaComponent } from '../tarjeta/tarjeta.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-busqueda',
  templateUrl: './busqueda.component.html',
  styleUrls: ['./busqueda.component.scss'],
  providers: [ApiService]
})
export class BusquedaComponent implements OnInit {

  lista:Array<any> = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
  odio1:string='1'
  odio2:string='2'
  odio3:string='3'
  municipio:string=''
  municipioURL:string='/?municipio='+this.municipio
  busqueda:Array<any>=[]
  keyword = 'nombre';
  data = [
    {
      id: 1,
      nombre: 'Georgia'
    },
     {
       id: 2,
       nombre: 'Usa'
     },
     {
       id: 3,
       nombre: 'England'
     }
  ];
  constructor(private router:Router, private activatedRoute: ActivatedRoute, private http: HttpClient, private api: ApiService) { }

  ngOnInit(): void {
    this.api.obtenerMunicipios().subscribe((res) =>
    {
      console.log('Res ', res.municipio);
      this.data = res.municipio
      //this.textoBuscar='id: '+res.municipio.id;
    });
    try{
      this.activatedRoute.queryParams.subscribe((data=>{
        this.municipio= data["municipio"]
        console.log('QueryParams', this.municipio)
        var ob = {"nombre":this.municipio}
        this.mandarBusqueda(ob)
      }))
    }catch{

    }
  }

  redirigirConMunicipio(textoBuscar:any){
    var texto = JSON.parse(JSON.stringify(textoBuscar)).nombre
    var url = "/?municipio="+texto
    console.log('redirigirConMunicipio', url)
    this.router.navigate([''], {queryParams:{"municipio":texto}})
  }

  mandarBusqueda(textoBuscar:any){
    var texto = JSON.parse(JSON.stringify(textoBuscar)).nombre
    console.log('recojo', texto)
    this.api.mandarMunicipio(texto).subscribe((res) =>
    {
      console.log('Res ', res);
      this.odio1=res.Odio
      this.odio2=res.OdioNoticias
      this.odio3=res.OdioComment
      this.transformarBusqueda(res.Quevers)
    });
  }

  transformarBusqueda(algo:any){
    this.busqueda=algo
  }
}
