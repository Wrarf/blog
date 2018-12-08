import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';

import { Post } from './post-model';

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

  getPost(pk): Observable<Post> {
  	return this.http.get<Post>(this.postListUrl + pk + '/');
  }
}
