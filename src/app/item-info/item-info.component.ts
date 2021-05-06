import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-item-info',
  templateUrl: './item-info.component.html',
  styleUrls: ['./item-info.component.css']
})
export class ItemInfoComponent implements OnInit {
  constructor(private http: HttpClient, private route: ActivatedRoute) { }

  id: number;
  item: any = {};

  // When the user clicks the Save button
  save(): void {
    // Make sure all of the fields are filled in.
    if (this.item.name && this.item.price && this.item.cost &&
      this.item.description && this.item.instock && this.item.category) {
      // Send the item to the database
      this.http.post<any>('http://127.0.0.1:5000/items/save', { item: this.item }).subscribe(result => {
        this.item = result.item;
      });
    }
  }

  // When the user clicks the Discontinue button
  discontinue(): void {
    this.http.post<any>('http://127.0.0.1:5000/items/discontinue',{ id: this.item.id, license_id: this.item.license.id }).subscribe(result => {
      console.log(result.item);
      this.item = result.item;
    });
  }

  ngOnInit(): void {
    this.route.params.subscribe( params => {
      this.id = params['id'];
      // Retrieves the current item based off the given ID.
      this.http.post<any>('http://127.0.0.1:5000/items/item', { id: this.id }).subscribe(result => {
          this.item = result.item;
      });
    });
  }

}
