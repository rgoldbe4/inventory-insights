import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import * as shajs from 'sha.js';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor(private http: HttpClient) { }

  admin: any = {};
  errors: Array<string> = [];
  licenses: Array<any> = [];

  register() {
      if (this.admin && this.admin.license && this.admin.first_name && this.admin.last_name && this.admin.email && this.admin.password) {
        // Encrypt the password
        this.admin.encrypted_password = shajs('sha256').update(this.admin.password).digest('hex');
        this.http.post<any>('http://127.0.0.1:5000/admin/register', this.admin).subscribe(result => {
          this.errors = result.errors;
          // Check if there were any errors. If not, login with registered administrator.
          if (this.errors.length == 0) {
            localStorage.setItem('admin_license_id', result.license.id);
            localStorage.setItem('administrator_id', result.administrator.id);
            window.location.href="admin";
          }
        });
      } else {
        this.errors.push('You need fill out all fields before you can continue.');
      }
  }

  ngOnInit(): void {
    // Retrieve all licenses
    this.http.get<any>('http://127.0.0.1:5000/license/all').subscribe(result => {
      this.licenses = result.licenses;
    });
  }

}
