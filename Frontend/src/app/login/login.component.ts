import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  // Auth tokens
  access: String;
  refresh: String;

  constructor(private authService: AuthService) { }

  loginForm = new FormGroup({
    username: new FormControl(''),
    password: new FormControl('')
  });

  login(): void {
    this.authService.login(this.loginForm.value).subscribe(
      (tokens) =>
        {
          this.authService.setUser(
            this.loginForm.value.username,
            tokens.access,
            tokens.refresh
          );
        }
    );
  }

}
