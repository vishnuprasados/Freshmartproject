import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MediatorService {


  fetchToken(){
    return localStorage.getItem("token")
  }


  getToken(data:any){

    let header=new Headers()
    header.append("Content-type",'application/json')
    let raw=JSON.stringify(data)

    let options={
      method:"POST",
      body:raw,
      headers:header
    }


    return fetch(`http://127.0.0.1:8000/token/`,options)

  }

  isAuthenticated(){
    return 'token' in localStorage
  }

  getProductList(){
   

    let header=new Headers()
    header.append("Content-type",'application/json')
    let token=this.fetchToken()
    if (token){
      header.append('Authorization',token)
    }
    let options={
      method:"GET",
    
      headers:header
    }

  return fetch(`http://127.0.0.1:8000/products/`,options)
}

getDetailView(id:any){
  
  let header=new Headers()
  header.append("Content-type",'application/json')
  let token=this.fetchToken()
  if (token){
    header.append('Authorization',token)
  }
  let options={
    method:"GET",
  
    headers:header
  }


  return fetch(`http://127.0.0.1:8000/products/${id}/`,options)

}
getRegisterView(data:any){
  let header=new Headers()
  header.append("Content-type",'application/json')
  let raw=JSON.stringify(data)

  let options={
    method:"POST",
    body:raw,
    headers:header
  }

  return fetch(`http://127.0.0.1:8000/user/`,options)
}

  constructor() { }
}
