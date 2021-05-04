import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-item-add',
  templateUrl: './item-add.component.html',
  styleUrls: ['./item-add.component.css']
})
export class ItemAddComponent implements OnInit {

  constructor(private http: HttpClient) { }

  item: any = {};

  // When the user adds the item
  addItem(): void {
    if (this.item.name && this.item.price && this.item.description && this.item.instock && this.item.cost && this.item.category){
      const licenseId = localStorage.getItem('admin_license_id');
      this.http.post<any>('http://127.0.0.1:5000/items/addItem', { item: this.item, license_id: licenseId }).subscribe(result => {
        window.location.href = 'admin/products/item/edit/' + result.item.id;
      });
    }
  }

  ngOnInit(): void {
  }

}
