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
  recommendedItems = [];


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

  addRecommendedToCart(recommended: any) {
    let cartId = localStorage.getItem('cart_id');
    this.http.post<any>('http://127.0.0.1:5000/cart/item/recommend/add',
      { item_id: recommended.id, cart_id: cartId }).subscribe(results => {
        this.recommendedItems = this.recommendedItems.filter(item => item !== recommended);
        this.cart = results.cart;
        if (this.recommendedItems.length == 0) {
          // Display more recommended items.
          this.http.post<any>('http://127.0.0.1:5000/cart/item/recommend', {cart_id: this.cart.id}).subscribe(results => {
            this.recommendedItems = results.items;
          });
        }
    });
  }

  ngOnInit(): void {
    // Retrieve the cart id and it's items.
    let cartId = localStorage.getItem('cart_id');
    this.http.post<any>('http://127.0.0.1:5000/cart', { id: cartId }).subscribe(results => {
      this.cart = results.cart;
      this.hasItems = this.cart.items.length > 0;
      // Acquire the cart's recommended items
      if (this.hasItems) {
        this.http.post<any>('http://127.0.0.1:5000/cart/item/recommend', {cart_id: this.cart.id}).subscribe(results => {
          this.recommendedItems = results.items;
        });
      }

    });
  }

}
