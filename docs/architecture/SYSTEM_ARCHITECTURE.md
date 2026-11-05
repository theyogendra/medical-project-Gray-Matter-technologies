# System Architecture

## Architectural goal

The project follows a modular, production-oriented architecture centered on a single PostgreSQL database and a shared API contract model.

## Layers

### Presentation layer

- React + TypeScript + Vite frontend
- Tailwind for styling
- React Router for navigation
- TanStack Query for async state
- React Hook Form + Zod for form validation

### Application layer

- NestJS backend with modular separation
- Controllers, services, DTOs, guards, and strategies
- Central validation, logging, and exception handling

### Data layer

- Prisma ORM
- PostgreSQL database
- Shared schema and migration management

### Cross-cutting concerns

- JWT auth
- RBAC structs
- CORS and environment-based configuration
- Audit-ready design
- CI/CD foundation

## Request flow

Client → API Route → Authentication Guard → Controller → Service → Prisma → PostgreSQL

## Security posture

- Validate inputs with NestJS pipes.
- Hash passwords with bcrypt.
- Use environment-based secrets.
- Keep all backend authorization checks server-side.
- Expose Swagger only in the configured development environment when appropriate.

## Scalability

This foundation is designed for subsequent module expansion without creating multiple databases or fragmented schema ownership.
