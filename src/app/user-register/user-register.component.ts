import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import * as shajs from 'sha.js';

@Component({
  selector: 'app-user-register',
  templateUrl: './user-register.component.html',
  styleUrls: ['./user-register.component.css']
})
export class UserRegisterComponent implements OnInit {

  constructor(private http: HttpClient) { }

  license: any = {};
  errors: Array<string> = [];
  user: any = {};

  // When the user clicks the Register button.
  register(): void {
    // Check if the user is valid
    if (this.user && this.user.first_name && this.user.last_name && this.user.email && this.user.password) {
      let password = this.user.password;
      this.user.encrypted_password = shajs('sha256').update(password).digest('hex');
      this.http.post<any>('http://127.0.0.1:5000/user/register', this.user).subscribe(result => {
        this.errors = result.errors;
        // Have the user automatically be logged in.
        localStorage.setItem('user_id', result.user.id);
        window.location.href='shop/products';
      });
    } else {
      this.errors.push('You need to fill out all fields.');
    }
  }

  ngOnInit(): void {
    // Check if a license is saved, if not, redirect
    if (localStorage.getItem('license_id') == null)
      window.location.href="shop";
    else {
      let license_id = localStorage.getItem('license_id');
      this.http.post<any>('http://127.0.0.1:5000/license', { id: license_id }).subscribe(result => {
        this.license = result.license;
      });
    }
  }

}
