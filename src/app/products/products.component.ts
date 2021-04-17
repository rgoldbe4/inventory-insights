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

  displayedItems: any[] = [];

  startPage: number = 0;
  endPage: number = 10;
  maxItems: number = 10;

  numItems: number = 10;

  pages: number[] = [];

  getDisplayedItems(start: number, end: number) {
    this.startPage = start;
    this.endPage = end;
    this.displayedItems = [];
    for (let i = start; i < end; i++) {
      if (this.items[i] != undefined)
        this.displayedItems.push(this.items[i]);
    }
    console.log(this.displayedItems);
  }

  ngOnInit(): void {
    this.http.get('http://127.0.0.1:5000/items/all').toPromise().then(result => {
      this.items = result['items'];
      this.numItems = result['items'].length;
      // Default from 0 to 10.
      this.getDisplayedItems(0, 10);
      this.pages = Array(Math.ceil(this.numItems / this.maxItems)).map((x, i)=>i);
    });
  }

}
