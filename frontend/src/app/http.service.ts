import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  postRoman(romanNumber: string){
    let httpHeaders = new HttpHeaders({
      'Content-Type' : 'application/json'
    }); 
    let body = {roman_number: romanNumber};
    return this.http.post('http://localhost:8000/converter/roman_to_int/', body,
      {
        headers: httpHeaders,
        observe: 'response'
      }
    );
  }

  postInt(intNumber: number){
    let httpHeaders = new HttpHeaders({
      'Content-Type' : 'application/json'
    }); 
    const body = {int_number: intNumber};
    return this.http.post('http://localhost:8000/converter/int_to_roman/', body,
      {
        headers: httpHeaders,
        observe: 'response'
      }
    );
  }
}
