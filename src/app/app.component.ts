import {Component, Injectable, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';

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
    this.http.get('http://127.0.0.1:5000/account/').toPromise().then(value => {
      console.log(value);
    });
  }

}
