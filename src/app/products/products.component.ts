import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  constructor(private http: HttpClient) { }

  // All items to display on the page.
  items: any = [];

  // Pagination
  displayedItems: any[] = []; // The items to display on the page.
  maxItems: number = 10; // The maximum number of items to display per page.
  numItems: number = 10; // The number of items in total
  pages: number[] = []; // The number of pages to display, in an array.

  // Update the displayedItems array with correct elements upon clicked.
  getDisplayedItems(start: number, end: number): void {
    start = start * 10;
    end = end * 10;
    this.displayedItems = [];
    for (let i = start; i < end; i++) {
      if (this.items[i] != undefined)
        this.displayedItems.push(this.items[i]);
    }
  }

  ngOnInit(): void {
    this.http.get('http://127.0.0.1:5000/items/all').toPromise().then(result => {
      this.items = result['items'];
      this.numItems = result['items'].length;
      // Default from 0 to 10.
      this.getDisplayedItems(0, 10);
      // Maps from 0 to numPages (0 to 10 would be [0,1,2,3,...,10])
      this.pages = Array(Math.ceil(this.numItems / this.maxItems)).map((x, i)=>i);
    });
  }

}
