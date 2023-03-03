import { HttpClient } from '@angular/common/http';
import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-vistalocal',
  templateUrl: './vistalocal.component.html',
  styleUrls: ['./vistalocal.component.scss']
})
export class VistalocalComponent implements OnInit {

  id:number = 0;
  datos:any = {}
  infocont:Array<any>=[]
  textotratar:string=""

  constructor(private route: ActivatedRoute, private http: HttpClient, private api: ApiService) {

   }

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];

    this.api.obtenerQueVerVistaLocal(this.id).subscribe((res) =>
    {
      //console.log('Res ', res.Quever[0]);
      this.datos = res.Quever[0]
      var textotratar=res.Quever[0].contacto
      textotratar=textotratar.replaceAll("\\n"," ")
      textotratar=textotratar.replaceAll("['"," ")
      textotratar=textotratar.replaceAll("'"," ")
      textotratar=textotratar.replaceAll("]"," ")
      textotratar=textotratar.replaceAll(", s/n"," ")

      this.infocont=textotratar.split(" ,")

      console.log("cont",this.infocont)
      //this.textoBuscar='id: '+res.municipio.id;

    /*
      var trigger = "['\n 91 171 13 49\n ', '\n Gran Vía\n ']",
      regexp = new RegExp('/[0-9]/gm'),
      test = regexp.test(trigger);
      console.log("REGEX ",test); // will display true

      const re = new regexp('-[0-9]+', 'g');
      console.log('2016-01-02|2019-03-07'.matchAll(re));
*/
    });
  }

}
