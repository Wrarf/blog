import { Component, OnInit } from '@angular/core';

import { PostService } from '../post.service';
import { PostPreview } from '../post-preview';

@Component({
  selector: 'app-post-list',
  templateUrl: './post-list.component.html',
  styleUrls: ['./post-list.component.css']
})
export class PostListComponent implements OnInit {
  postPreviews: PostPreview[];

  constructor(private postService: PostService) { }

  getPostPreview(): void {
    this.postService.getPostPreview().subscribe(
      res => this.postPreviews = res.results
    );
  }

  ngOnInit() {
    this.getPostPreview();
  }

}
