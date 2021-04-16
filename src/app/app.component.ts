import {Component, Injectable, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import * as shajs from 'sha.js';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
@Injectable()
export class AppComponent implements OnInit {
  title = 'inventory-insights';
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    let password = shajs('sha256').update('password').digest('hex');
  }

}
