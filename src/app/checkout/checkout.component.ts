import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent implements OnInit {

  constructor(private http: HttpClient) { }

  cart: any = {};
  order: any = null;

  // When the user clicks the "place order" button
  placeOrder(): void {
    let userId = localStorage.getItem('user_id');
    let cartId = localStorage.getItem('cart_id');
    // Send cart to the backend and convert it to an order
    this.http.post<any>('http://127.0.0.1:5000/cart/checkout', { cart_id: cartId, user_id: userId }).subscribe(results => {
      this.order = results.order;
      this.order.total = 0;
      this.order.items.forEach(item => {
        this.order.total += item.price;
      });
      // Remove the cart ID.
      localStorage.removeItem('cart_id');
    });
  }

  ngOnInit(): void {
    let cartId = localStorage.getItem('cart_id');
    this.http.post<any>('http://127.0.0.1:5000/cart', { id: cartId }).subscribe(results => {
      this.cart = results.cart;
      this.cart.total = 0;
      this.cart.items.forEach(item => {
        this.cart.total += item.price;
      });
    });
  }

}
