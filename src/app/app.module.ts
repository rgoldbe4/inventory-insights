import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { ItemComponent } from './item/item.component';
import { HttpClientModule } from '@angular/common/http';

import { Injectable } from '@angular/core';
import { AdminComponent } from './admin/admin.component';
import { ShopComponent } from './shop/shop.component';
import { AdminNavComponent } from './admin-nav/admin-nav.component';

@NgModule({
  declarations: [
    AppComponent,
    ItemComponent,
    AdminComponent,
    ShopComponent,
    AdminNavComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot([
      { path: 'admin', component: AdminComponent },
      { path: 'shop', component: ShopComponent },
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
