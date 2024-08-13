import { Component, OnInit } from '@angular/core';
import { MediatorService } from '../mediator.service';
import { Router } from '@angular/router';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{

  form1=new FormGroup({
    'username':new FormControl(),
    'password':new FormControl()
  })

  getUserdata(){

    // console.log(this.form1.value);
    this.service.getToken(this.form1.value).then(res=>res.json()).then(data=>{
      console.log(data); 
      if('token' in data){
        let token="Token "+data.token
        localStorage.setItem("token",token)
        this.router.navigate(['products'])
      }
      else{
        alert('invalid credentials')
      }
      

    
  })
   }

   ngOnInit(): void {
     
   }

  constructor(public service:MediatorService,public router:Router){}

}
