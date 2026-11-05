# Deployment Guide

## Local deployment

1. Install dependencies.
2. Configure `.env` values.
3. Start PostgreSQL with Docker Compose.
4. Run Prisma migration generation and execution.
5. Start frontend and backend.

## Production guidance

- Use a managed PostgreSQL service.
- Configure secure environment variables.
- Enable CI/CD verification for lint, test, and production build.
- Use a reverse proxy or platform ingress.
- Keep secrets and credentials outside the source tree.

## Recommended deployment pattern

- Frontend: Vite static build or hosting platform.
- API: containerized NestJS service.
- Database: managed PostgreSQL instance with backups.
