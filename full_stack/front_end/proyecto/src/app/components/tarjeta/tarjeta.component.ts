import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-tarjeta',
  templateUrl: './tarjeta.component.html',
  styleUrls: ['./tarjeta.component.scss']
})
export class TarjetaComponent implements OnInit {

  @Input() indiceLocalidad:number = 1;
  @Input() imagen:string = 'https://img1.ak.crunchyroll.com/i/spire2-tmb/e4040cdee30fc1de1da0f5897adcfed11403179939_main.jpg';
  @Input() nombre:string = '';

  constructor() { }

  ngOnInit(): void { }

}
