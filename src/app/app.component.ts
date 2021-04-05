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
    let testData = {
        'first_name': 'Ryan',
        'last_name': 'Goldberg',
        'email': 'admin@buffsovernexus.com',
        'password': password
    };
    console.log(password)
    this.http.post('http://127.0.0.1:5000/account/create/', testData).toPromise().then(result => {
      console.log(result);
    })
  }

}
