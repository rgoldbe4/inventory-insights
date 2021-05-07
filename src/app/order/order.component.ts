import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  constructor(private http: HttpClient, private route: ActivatedRoute) { }
  orders: any = { };
  ngOnInit(): void {
    let id = localStorage.getItem("user_id");
    this.http.post<any>('http://127.0.0.1:5000/user', { id: id }).subscribe(result => {
      console.log(result);
      this.orders = result.user.orders;
    });
  }
}
