import {Component, Injectable, OnInit} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as shajs from 'sha.js';
import {getHelper} from '@angular/core/schematics/migrations/renderer-to-renderer2/helpers';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
@Injectable()
export class LoginComponent implements OnInit {

  title = 'inventory-insights';
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    const password = shajs('sha256').update('test').digest('hex');
  }

}
