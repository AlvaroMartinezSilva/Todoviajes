import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';//funciones ngif, ngfor etc.
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FooterComponent } from './components/footer/footer.component';
import { LoginComponent } from './components/login/login.component';
import { BusquedaComponent } from './components/busqueda/busqueda.component';
import { TarjetaComponent } from './components/tarjeta/tarjeta.component';
import { VistalocalComponent } from './components/vistalocal/vistalocal.component';//para hacer llamadas http
import { AutocompleteLibModule} from 'angular-ng-autocomplete';
import { AdminComponent } from './components/admin/admin.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';//para autocompletar campos
import { MatButtonModule } from '@angular/material/button';
import { ChartComponent } from './components/chart/chart.component';
import { TokenInterceptor } from './interceptors/token.interceptor';
//import { NgbModule } from '@ng-bootstrap/ng-bootstrap';//bootstrap
import { NgChartsModule } from 'ng2-charts';
import { UsersComponent } from './components/users/users.component';
import { NuevoUserComponent } from './components/nuevo-user/nuevo-user.component';
import { EditarUserComponent } from './components/editar-user/editar-user.component';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    LoginComponent,
    BusquedaComponent,
    TarjetaComponent,
    VistalocalComponent,
    AdminComponent,
    ChartComponent,
    UsersComponent,
    NuevoUserComponent,
    EditarUserComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    AutocompleteLibModule,
    BrowserAnimationsModule,
    MatButtonModule,
    NgChartsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi:true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
