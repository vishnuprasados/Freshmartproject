import { Component, OnInit } from '@angular/core';
import { MediatorService } from '../mediator.service';
import { Router } from '@angular/router';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {


  form2=new FormGroup({
    'first_name':new FormControl(),
    'last_name':new FormControl(),
    'email':new FormControl(),
    'username':new FormControl(),
    'password':new FormControl()
  })

  getRegistrationdata(){

    // console.log(this.form1.value);
    this.service.getRegisterView(this.form2.value).then(res=>res.json()).then(data=>{
      console.log(data); 

      if('msg' in data){
        alert('invalid')
       
      }
      else{
        alert('success')
        this.router.navigate([''])
      }
    
      
      

    
  })
   }

   ngOnInit(): void {
     
   }

  constructor(public service:MediatorService,public router:Router){}

}
