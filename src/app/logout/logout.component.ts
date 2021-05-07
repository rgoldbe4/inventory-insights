import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    localStorage.removeItem("administrator_id");
    localStorage.removeItem("admin_license_id");
    localStorage.removeItem("user_id");
    localStorage.removeItem('license_id');
    window.location.href="";
  }

}
