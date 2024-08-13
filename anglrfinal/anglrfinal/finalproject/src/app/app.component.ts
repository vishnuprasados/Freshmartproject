import { Component } from '@angular/core';
import { MediatorService } from './mediator.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'finalproject';
  isLoggedIn=false

  constructor(private service:MediatorService,private router:Router){
    this.isLoggedIn=this.service.isAuthenticated()
  }
}
