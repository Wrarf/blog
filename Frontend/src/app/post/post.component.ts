import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";

import { Observable } from 'rxjs';

import { PostService } from '../post.service';

import { Post } from '../post-model';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  post: Post;

  constructor(
    private postService: PostService,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    let pk = this.route.snapshot.paramMap.get('pk');
    this.getPost(pk);
  }

  getPost(pk): void {
    this.postService.getPost(pk).subscribe(
      res => this.post = res
    );
  }

}
