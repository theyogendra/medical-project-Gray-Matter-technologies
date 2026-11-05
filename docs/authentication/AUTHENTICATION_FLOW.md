# Authentication Flow

## Overview

The application uses JWT access and refresh tokens with server-side validation. Passwords are never stored in plaintext.

## Flow

1. User submits login credentials.
2. Backend validates email and password.
3. Password is compared using `bcrypt`.
4. JWT access token and refresh token are created.
5. Protected routes validate the bearer token with the JWT strategy.
6. User role from the token is checked by authorization guards.

## Security controls

- Password hashing with bcrypt.
- JWT secret stored in env values.
- Protected routes enforced on the server.
- CORS restricted to configured origin.
- JWT expiration and refresh strategy scaffolded.

## Future work

- Logout token blacklisting.
- Refresh token rotation and revoke flows.
- Role permission enforcement per API route.
