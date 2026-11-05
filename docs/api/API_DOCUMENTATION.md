# API Documentation

## API foundation

The backend exposes a versioned REST API under `/api/v1` and includes Swagger documentation at `/api/docs`.

## Endpoints

### Authentication

| Method | Endpoint | Purpose | Auth |
|---|---|---|---|
| POST | `/api/v1/auth/login` | User login and JWT issuance | No |
| GET | `/api/v1/health` | Health check | No |
| GET | `/api/v1/users` | Read users | Yes |
| POST | `/api/v1/users` | Create a user | Yes |

## Response envelope

The foundation uses standard NestJS JSON responses. Detailed business response envelopes can be added when each domain module is implemented.

## Authentication requirements

- JWT bearer token required for protected routes.
- Access token and refresh token strategy is scaffolded.
- Secret values must be supplied through environment configuration.

## Validation rules

- Email validation required for login and user creation.
- Password minimum length enforced.
- Role values limited to a defined enum.
- Request bodies validated by NestJS `ValidationPipe`.
