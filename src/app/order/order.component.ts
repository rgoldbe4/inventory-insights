import {Component, Injectable, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
@Injectable()
export class OrderComponent implements OnInit {

  constructor(private http: HttpClient, private route: ActivatedRoute) { }

  // All orders to display on the page.
  orders: any = [];

  // Pagination
  displayedOrders: any[] = []; // The items to display on the page.
  maxOrders: number = 6; // The maximum number of items to display per page.
  numOrders: number = 10; // The number of items in total
  pages: number[] = []; // The number of pages to display, in an array.
  currentPage: number = 0;
  maxPages: number = 0;

  // Update the displayedItems array with correct elements upon clicked.
  getDisplayedItems(start: number, end: number): void {
    this.currentPage = start;
    start = start * this.maxOrders;
    end = end * this.maxOrders;
    this.displayedOrders = [];
    for (let i = start; i < end; i++) {
      if (this.orders[i] != undefined)
        this.displayedOrders.push(this.orders[i]);
    }
  }
  // This updates the pagination variables on the page any time it updates.
  updatePagination(result: any) : void {
    this.numOrders = result['orders'].length;
    this.maxPages = Math.ceil(this.numOrders / this.maxOrders);
    // Default from 0 to 10.
    this.getDisplayedItems(this.currentPage, this.currentPage + 1);
    // Maps from 0 to numPages (0 to 10 would be [0,1,2,3,...,10])
    this.pages = Array(this.maxPages).map((x, i)=>i);
  }

  ngOnInit(): void {
    let id = localStorage.getItem("user_id");
    this.http.post<any>('http://127.0.0.1:5000/user', { id: id }).subscribe(result => {
      this.orders = result.user.orders;
      this.updatePagination(result.user);
    });
  }
}
