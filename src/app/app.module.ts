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
import { ProductsComponent } from './products/products.component';
import { ItemInfoComponent } from './item-info/item-info.component';
import {FormsModule} from '@angular/forms';
import { ItemAddComponent } from './item-add/item-add.component';
import { CartComponent } from './cart/cart.component';
import { SplashComponent } from './splash/splash.component';
import { LoginComponent } from './login/login.component';
import { SplashNavComponent } from './splash-nav/splash-nav.component';
import { LogoutComponent } from './logout/logout.component';
import { AdminAccountComponent } from './admin-account/admin-account.component';
import { ShopNavComponent } from './shop-nav/shop-nav.component';
import { UserLoginComponent } from './user-login/user-login.component';
import { UserRegisterComponent } from './user-register/user-register.component';
import { UserComponent } from './user/user.component';
import { OrderComponent } from './order/order.component';
import { ShopProductsComponent } from './shop-products/shop-products.component';
import { ShopProductComponent } from './shop-product/shop-product.component';

@NgModule({
  declarations: [
    AppComponent,
    ItemComponent,
    AdminComponent,
    ShopComponent,
    AdminNavComponent,
    ProductsComponent,
    ItemInfoComponent,
    ItemAddComponent,
    CartComponent,
    SplashComponent,
    LoginComponent,
    SplashNavComponent,
    LogoutComponent,
    AdminAccountComponent,
    ShopNavComponent,
    UserLoginComponent,
    UserRegisterComponent,
    UserComponent,
    OrderComponent,
    ShopProductsComponent,
    ShopProductComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot([
      // Base Paths
      {path: '', component: SplashComponent},
      {path: 'admin', component: AdminComponent},
      {path: 'shop', component: ShopComponent},

      // Administrator Paths
      {path: 'admin/products', component: ProductsComponent},
      {path: 'admin/products/item/edit/:id', component: ItemComponent},
      {path: 'admin/products/item/info/:id', component: ItemInfoComponent},
      {path: 'admin/products/item/add', component: ItemAddComponent},
      {path: 'admin/login', component: LoginComponent}, // Administrator Login
      {path: 'logout', component: LogoutComponent}, // Global logout (user and admin)
      {path: 'admin/account', component: AdminAccountComponent},

      // Shop Paths
      {path: 'user/account', component: UserComponent},
      {path: 'user/login', component: UserLoginComponent},
      {path: 'user/register', component: UserRegisterComponent},
      {path: 'shop/cart', component: CartComponent},
      {path: 'shop/order', component: OrderComponent},
      {path: 'shop/products', component: ShopProductsComponent},
      {path: 'shop/products/product/:id', component: ShopProductComponent}
    ]),
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
