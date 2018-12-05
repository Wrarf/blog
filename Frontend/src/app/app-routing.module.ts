import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './login/login.component'
import { PostListComponent } from './post-list/post-list.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '', component: PostListComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
