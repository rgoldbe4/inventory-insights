import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {

  constructor(private http: HttpClient) { }

  cart: any = {};
  hasItems = false;

  remove(item: any) {
    let cartId = localStorage.getItem('cart_id');
    // Remove the item from the cart, then update the cart list.
    this.http.post<any>('http://127.0.0.1:5000/cart/item/remove', { cart_id: cartId, item_id: item.id })
      .subscribe(results => {
        // Returns with cart and item
        this.cart = results.cart;
        this.hasItems = this.cart.items.length > 0;
    });
  }

  ngOnInit(): void {
    // Retrieve the cart id and it's items.
    let cartId = localStorage.getItem('cart_id');
    this.http.post<any>('http://127.0.0.1:5000/cart', { id: cartId }).subscribe(results => {
      this.cart = results.cart;
      this.hasItems = this.cart.items.length > 0;
    });
  }

}
