import {Component, Injectable, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-admin-nav',
  templateUrl: './admin-nav.component.html',
  styleUrls: ['./admin-nav.component.css']
})
@Injectable()
export class AdminNavComponent implements OnInit {

  constructor(private http: HttpClient) { }

  administrator: any = {};

  ngOnInit(): void {

    // Check if the Admin is logged in. Otherwise, redirect to the login screen.
    if (localStorage.getItem("administrator_id") == null) {
      window.location.href="admin/login";
    } else {
      // Update the Administrator Button with the Admin's name.
      let admin_id = localStorage.getItem("administrator_id");
      this.http.post<any>('http://127.0.0.1:5000/admin', { id: admin_id }).subscribe(result => {
        this.administrator = result.admin;
      });
    }
  }


}
