import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';

import { User } from './user';

const httpOptions = {
	headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  loginUrl = 'http://localhost:8000/api/token/';

  currentUser: User = new User();

  constructor(private http: HttpClient) { }

  login(credentials): Observable<any> {
  	return this.http.post(this.loginUrl, credentials, httpOptions);
  }

  setUser(username, access, refresh): void {
  	this.currentUser.username = username
  	this.currentUser.access_token = access
  	this.currentUser.refresh_token = refresh
  }
}
