import { Component, OnInit } from '@angular/core';
import { MediatorService } from '../mediator.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-productlist',
  templateUrl: './productlist.component.html',
  styleUrls: ['./productlist.component.css']
})
export class ProductlistComponent implements OnInit {

  products:any

  ngOnInit(): void {
    this.service.getProductList().then(res=>res.json().then(data=>this.products=data))
    console.log(this.products)
  }

  redirectToDetail(id:any){

    this.rout.navigate(['detail',id])
    
    
  }

  constructor(public service:MediatorService,public rout:Router){}

}
