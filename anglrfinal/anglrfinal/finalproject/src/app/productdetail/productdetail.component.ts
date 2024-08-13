import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MediatorService } from '../mediator.service';

@Component({
  selector: 'app-productdetail',
  templateUrl: './productdetail.component.html',
  styleUrls: ['./productdetail.component.css']
})
export class ProductdetailComponent implements OnInit{

  product:any

  ngOnInit(): void {
    let id=this.route.snapshot.paramMap.get('id')
    this.service.getDetailView(id).then(res=>res.json()).then(res=>this.product=res)
    
  }
 constructor(public route:ActivatedRoute,public service:MediatorService){}

 
  
  
}


