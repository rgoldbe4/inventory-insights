import {Component, Injectable, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
@Injectable()
export class ProductsComponent implements OnInit {

  constructor(private http: HttpClient, private route: ActivatedRoute) { }

  // All items to display on the page.
  items: any = [];
  showDiscontinued: boolean = false; // Whether or not to show discontinued items.

  // Pagination
  displayedItems: any[] = []; // The items to display on the page.
  maxItems: number = 10; // The maximum number of items to display per page.
  numItems: number = 10; // The number of items in total
  pages: number[] = []; // The number of pages to display, in an array.
  currentPage: number = 0;
  maxPages: number = 0;

  // Toggle displaying discontinued items
  toggleDiscontinued(): void {
    this.showDiscontinued = !this.showDiscontinued;
  }

  // Update the displayedItems array with correct elements upon clicked.
  getDisplayedItems(start: number, end: number): void {
    this.currentPage = start;
    start = start * this.maxItems;
    end = end * this.maxItems;
    this.displayedItems = [];
    for (let i = start; i < end; i++) {
      if (this.items[i] != undefined)
        this.displayedItems.push(this.items[i]);
    }
  }

  // This updates the pagination variables on the page any time it updates.
  updatePagination(result: any) : void {
    this.numItems = result['items'].length;
    this.maxPages = Math.ceil(this.numItems / this.maxItems);
    // Default from 0 to 10.
    this.getDisplayedItems(this.currentPage, this.currentPage + 1);
    // Maps from 0 to numPages (0 to 10 would be [0,1,2,3,...,10])
    this.pages = Array(this.maxPages).map((x, i)=>i);
  }

  // Discontinue a product.
  discontinue(id: number) : void {
    let license_id = localStorage.getItem("admin_license_id");
    this.http.post<any>('http://127.0.0.1:5000/items/discontinue',{ id: id, license_id: license_id })
      .subscribe(discontinue_result => {
        // Reacquire all of the items from the list.
        this.http.post<any>('http://127.0.0.1:5000/items/all', { license_id: license_id })
          .subscribe(result => {
            this.items = result.items;
            this.updatePagination(result);
          }
        );

      }
    );
  }

  ngOnInit(): void {
    let license_id = localStorage.getItem("admin_license_id");
    this.http.post<any>('http://127.0.0.1:5000/items/all', { license_id: license_id }).subscribe(result => {
      this.items = result.items;
      this.updatePagination(result);
    });
  }

}
