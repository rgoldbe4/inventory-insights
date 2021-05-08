import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.css']
})
export class ShopComponent implements OnInit {

  constructor(private http: HttpClient) { }

  licenses: Array<any> = [];

  selectLicense(id: number) {
    localStorage.setItem('license_id', id + '');
    // Go to the shop's product page, which is the shop splash page.
    window.location.href="shop/products";
  }

  ngOnInit(): void {
    // Grab all licenses (shops)
    this.http.get<any>('http://127.0.0.1:5000/license/all').subscribe(result => {
      this.licenses = result.licenses;
      // Now grab all items from the license
      this.licenses.forEach( (license, index) => {
        this.http.post<any>('http://127.0.0.1:5000/items/all', { license_id: license.id }).subscribe(result => {
            this.licenses[index].first_example = result.items[0];
            this.licenses[index].second_example = result.items[1];
            this.licenses[index].third_example = result.items[2];
        });
      })
    });
  }

}
