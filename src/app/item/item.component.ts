import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css']
})


export class ItemComponent implements OnInit {
  constructor(private http: HttpClient, private route: ActivatedRoute) { }

  id: number;
  item: any = {};

  ngOnInit(): void {
    /*
    this.route.params.subscribe( params => {
      this.id = params['id'];
      this.http.post('http://127.0.0.1:5000/items/item', { id: this.id }).toPromise().then(result => {
          this.item = result['item'];
      });
    })
     */
  }

}
