import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  constructor(private http: HttpClient) { }

  items: any = [];

  ngOnInit(): void {

    this.http.get('http://127.0.0.1:5000/items/all').toPromise().then(result => {
      this.items = result['items'];
    });
  }

}
