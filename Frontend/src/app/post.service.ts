import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PostService {
  postListUrl = 'http://localhost:8000/posts/';
  previewsUrl = 'http://localhost:8000/previews/';

  constructor(private http: HttpClient) { }

  getPostPreview(): Observable<any> {
  	return this.http.get<any>(this.previewsUrl);
  }
}
