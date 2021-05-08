import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import * as shajs from 'sha.js';

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent implements OnInit {

  constructor(private http: HttpClient) { }

  user: any = {};
  errors: Array<string> = [];
  license: any = {};

  login(): void {
    // Check if user entered in all fields
    if (this.user && this.user.email && this.user.password) {
      // Now, check if the user is valid.
      let password = this.user.password;
      this.user.password = "";
      this.user.encrypted_password = shajs('sha256').update(password).digest('hex');
      this.http.post<any>('http://127.0.0.1:5000/user/login', this.user).subscribe(result => {
        this.errors = result.errors;
        if (this.errors.length == 0 && result.user) {
          // Store the user in the session.
          localStorage.setItem('user_id', result.user.id);
          // Redirect to the product page of the shop they are currently in.
          window.location.href="shop/products";
        }
      });
    }
  }

  ngOnInit(): void {
    // Check if a license is saved, if not, redirect
    if (localStorage.getItem('license_id') == null)
      window.location.href="shop"
    else {
      let license_id = localStorage.getItem('license_id');
      this.http.post<any>('http://127.0.0.1:5000/license', { id: license_id}).subscribe(result => {
        this.license = result.license;
      });
    }
  }

}
