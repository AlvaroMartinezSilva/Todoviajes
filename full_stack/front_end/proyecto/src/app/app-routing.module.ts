import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { BusquedaComponent } from './components/busqueda/busqueda.component';
import { TarjetaComponent } from './components/tarjeta/tarjeta.component';
import { VistalocalComponent } from './components/vistalocal/vistalocal.component';
import { AdminComponent } from './components/admin/admin.component';//para autocompletar campos
import { ChartComponent } from './components/chart/chart.component';
import { RolesGuard } from './guards/roles.guard';
import { UsersComponent } from './components/users/users.component';
import { NuevoUserComponent } from './components/nuevo-user/nuevo-user.component';
import { EditarUserComponent } from './components/editar-user/editar-user.component';


const routes: Routes = [
{
  path:'', component: BusquedaComponent

},{

  path:'login', component: LoginComponent

},{

  path:'admin', component: AdminComponent, canActivate:[RolesGuard]

},{
  path:'users', component:UsersComponent, canActivate:[RolesGuard]
},{
  path:'crear', component:NuevoUserComponent, canActivate:[RolesGuard]
},{
  path:'editar', component:EditarUserComponent, canActivate:[RolesGuard]
},{

  path:'tarjeta', component: TarjetaComponent

},{

  path:'vistalocal/:id', component: VistalocalComponent

},{
  path:'grafica', component: ChartComponent, canActivate:[RolesGuard]
},{

  path:'**', redirectTo: ''//para una ruta desconocida que se dirija a la pagina principal

}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
