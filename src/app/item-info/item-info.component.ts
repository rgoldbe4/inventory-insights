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
  sales: Array<number> = [];

  // When the user clicks the Save button
  save(): void {
    // Make sure all of the fields are filled in.
    if (this.item.name && this.item.price && this.item.cost &&
      this.item.description && this.item.instock && this.item.category) {
      // Send the item to the database
      this.http.post<any>('http://127.0.0.1:5000/items/save', { item: this.item }).subscribe(result => {
        this.item = result.item;
        this.updateItemValues()
      });
    }
  }

  // When the user clicks the Discontinue button
  discontinue(): void {
    this.http.post<any>('http://127.0.0.1:5000/items/discontinue',{ id: this.item.id, license_id: this.item.license.id }).subscribe(result => {
      console.log(result.item);
      this.item = result.item;
      this.updateItemValues()
    });
  }

  ngOnInit(): void {
    this.route.params.subscribe( params => {
      this.id = params['id'];
      // Retrieves the current item based off the given ID.
      this.http.post<any>('http://127.0.0.1:5000/items/item', { id: this.id }).subscribe(result => {
          this.item = result.item;
          this.updateItemValues()
      });
      // Grab graph information from the item.
      this.http.post<any>('http://127.0.0.1:5000/items/monthlySales', { item_id: this.id }).subscribe(result => {
        this.sales = result.sales;
        this.chartDatasets = [
          { data: this.sales, label: 'Monthly Sales' }
        ]
      });
    });
  }

  updateItemValues(): void {
      this.item.profit = this.item.price - this.item.cost;
      this.item.total_price = this.item.price * this.item.instock;
      this.item.total_cost = this.item.cost * this.item.instock;
      this.item.total_profit = this.item.profit * this.item.instock;
  }

  public chartType: string = 'line';

  public chartDatasets: Array<any> = [
    { data: this.sales, label: 'Monthly Sales' },
  ];

  public chartLabels: Array<any> = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                                    'October', 'November', 'December'];

  public chartColors: Array<any> = [
    {
      backgroundColor: 'rgba(105, 0, 132, .2)',
      borderColor: 'rgba(200, 99, 132, .7)',
      borderWidth: 2,
    },
    {
      backgroundColor: 'rgba(0, 137, 132, .2)',
      borderColor: 'rgba(0, 10, 130, .7)',
      borderWidth: 2,
    }
  ];

  public chartOptions: any = {
    responsive: true
  };
  public chartClicked(e: any): void { }
  public chartHovered(e: any): void { }

}
