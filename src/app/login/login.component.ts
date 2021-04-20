import {Component, Injectable, OnInit} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as shajs from 'sha.js';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
@Injectable()
export class LoginComponent implements OnInit {

  title = 'inventory-insights';
  constructor(private http: HttpClient) { }

  // Declare variables needed on the page and for validation.
  admin: any = {};
  errors: Array<string> = [];

  // Event when the user logs in
  login(): void {
    // Reset errors on each click.
    this.errors = [];

    // Determine if both email and password were filled out.
    if (this.admin.email && this.admin.password) {
      this.admin.encryped_password = shajs('sha256').update(this.admin.password).digest('hex');
      // Reset password field so it does not appear in the POST request.
      this.admin = {};
      // Communicate with the backend to ask if the administrator exists with those credentials.
      this.http.post<any>('http://127.0.0.1:5000/account/login', this.admin).subscribe(result => {
        // Check if the administrator exists.
        if (!result.exists) {
          this.errors.push("The email and password combination are not found.");
        } else {
          // This saves the ID of administrator so we can check if they are in session for the future.
          localStorage.setItem("administrator_id", result.administrator.id);
          console.log(localStorage.getItem("administrator_id"));
        }
      });
    } else {
      // Alert of an error.
      this.errors.push("You must enter in both an email and password to continue.");
    }
  }

  ngOnInit(): void {

  }

}
