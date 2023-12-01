import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// MY COMPONENTS
import { ProductoComponent } from './producto/producto.component';

// PRIME NG MODULES
import { TableModule } from 'primeng/table';
import { DropdownModule } from 'primeng/dropdown';
import { ButtonModule } from 'primeng/button';
import { DialogModule } from 'primeng/dialog';
import { InputTextModule } from 'primeng/inputtext';
import { InputNumberModule } from 'primeng/inputnumber';
import { ConfirmDialogModule } from 'primeng/confirmdialog';
import { ToastModule } from 'primeng/toast';




@NgModule({
  declarations: [
    AppComponent,
    ProductoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    TableModule,
    ButtonModule,
    DialogModule,
    FormsModule,
    InputTextModule,
    InputNumberModule,
    ConfirmDialogModule,
    ToastModule,
    DropdownModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule { }
