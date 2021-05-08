import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  constructor(private http: HttpClient) { }

  user: any = { };

  save(): void {
    // Check if all entries are filled
    if (this.user.first_name && this.user.last_name && this.user.email) {
      // Update the user in the database
      this.http.post<any>('http://127.0.0.1:5000/user/save', this.user).subscribe(result =>{
        console.log("This.user: " + this.user + " result.user: " + result.user);
        this.user = result.user;
      });
    }
  }

  ngOnInit(): void {
    // Get the user from the database and populate it here.
    let user_id = localStorage.getItem("user_id");
    this.http.post<any>('http://127.0.0.1:5000/user', { id: user_id }).subscribe(result => {
      this.user = result.user;
      this.user.full_name = this.user.first_name + " " + this.user.last_name;
    });
  }

}
