import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SmarthomeService {
  url = 'http://127.0.0.1:5000/';
  constructor(private http: HttpClient) { }

  get_last_measurement(measurement:string, device:string): Observable<any>{
    return this.http.get<any>(this.url + 'measurement/' + measurement + '/' + device);
  }
}
