import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-item-add',
  templateUrl: './item-add.component.html',
  styleUrls: ['./item-add.component.css']
})
export class ItemAddComponent implements OnInit {

  constructor() { }

  item: any = {}

  // When the user adds the item
  addItem(): void {
    console.log(this.item);
  }

  ngOnInit(): void {
  }

}
