import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-shop-product',
  templateUrl: './shop-product.component.html',
  styleUrls: ['./shop-product.component.css']
})
export class ShopProductComponent implements OnInit {

  constructor(private http: HttpClient, private route: ActivatedRoute) { }

  id: number;
  item: any = {};

  // When the user clicks Add To Cart
  addToCart(): void {
    this.http.post<any>('http://127.0.0.1:5000/cart/',{ id: this.item.id, license_id: this.item.license.id }).subscribe(result => {
      this.item = result.item;
    });
  }

  ngOnInit(): void {
    this.route.params.subscribe( params => {
      this.id = params['id'];
      // Retrieves the current item based off the given ID.
      this.http.post<any>('http://127.0.0.1:5000/items/item', { id: this.id }).subscribe(result => {
          this.item = result.item;
      });
    });
  }

}
