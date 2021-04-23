import {Component, Injectable, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-admin-account',
  templateUrl: './admin-account.component.html',
  styleUrls: ['./admin-account.component.css']
})
@Injectable()
export class AdminAccountComponent implements OnInit {

  constructor(private http: HttpClient) { }

  administrator: any = { };

  ngOnInit(): void {
    // Get the administrator from the database and populate it here.
    let admin_id = localStorage.getItem("administrator_id");
    this.http.post<any>('http://127.0.0.1:5000/admin', { id: admin_id }).subscribe(result => {
      this.administrator = result.admin;
      this.administrator.full_name = this.administrator.first_name + " " + this.administrator.last_name;
      console.log(this.administrator);
    });
  }

}
