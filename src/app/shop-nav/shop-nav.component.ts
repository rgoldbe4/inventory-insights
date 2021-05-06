import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-shop-nav',
  templateUrl: './shop-nav.component.html',
  styleUrls: ['./shop-nav.component.css']
})
export class ShopNavComponent implements OnInit {

  constructor(private http: HttpClient) { }

  user = {};

  ngOnInit(): void {
    // Check if the user is logged in.
    if (localStorage.getItem('user_id') !== null) {
      // Acquire the user account.
      let user_id = localStorage.getItem('user_id');
      this.http.post<any>('http://127.0.0.1:5000/user', { id: user_id }).subscribe(result => {
        this.user = result.user;
      });
    } else {
        // User is not logged in. Move them to login page.
        window.location.href="user/login";
    }

    // Check if they are somehow accessing a shop when they shouldn't be...
    if (localStorage.getItem('license_id') == null) {
        window.location.href = "shop";
    }
  }

}
