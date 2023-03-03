import { Component, OnInit } from '@angular/core';
import { ViewRef } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})

   
export class NavbarComponent implements OnInit {

  constructor(private router: Router, private api: ApiService) {
    
   }
   
  ngOnInit(): void {
    
  }

  usuarioRegistrado(): boolean{
    return this.api.isLogin()
  }
  
  logOut(): void{
    this.api.borrarToken();
    this.router.navigate([""])
  }
  
}
//private route: ActivatedRoute, private api: ApiService, private router: Router
