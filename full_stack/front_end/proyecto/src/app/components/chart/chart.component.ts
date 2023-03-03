import { Component, OnInit } from '@angular/core';
import {Chart, ChartConfiguration, ChartItem, registerables} from 'node_modules/chart.js'
import { ApiService } from 'src/app/services/api.service';
import { HttpClient } from '@angular/common/http';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss']
})
export class ChartComponent implements OnInit {
  valorSelect = ""
  constructor(private http: HttpClient, private api: ApiService) { }
  busqueda:Array<any>=[]
  nombreMunicipio:Array<string>=[]
  numbusquedas:Array<number>=[]
  datosBusqueda:any=[];
  ngOnInit(): void {

    this.datosBusqueda = this.api.datosgrafica().subscribe((res)=>{

      this.busqueda=res.data
    console.log("pedirBusquedas", this.busqueda);
    this.nombreMunicipio = this.busqueda.map(res => res.id);

    this.numbusquedas = this.busqueda.map(res => res.count);

    console.log("ba", this.nombreMunicipio);
    this.createChart()

    });
  }

  createChart(): void {

    Chart.register(...registerables);

    const data = {
    labels: this.nombreMunicipio,
    datasets: [{
      label: 'Visitas',
      backgroundColor: 'rgb(255, 166, 22)',
      labels: '#ffffff',
      data: this.numbusquedas
    }]
};

const options = {
  scales: {
    y: {
      beginAtZero: true,
      display: false
    }
  }
}

const config: ChartConfiguration = {
  type: 'bar',
  data: data,
  options: options
}

const chartItem: ChartItem = document.getElementById('my-chart') as ChartItem

new Chart(chartItem, config)


  }




}
