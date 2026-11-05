# Development Setup

## Prerequisites

- Node.js 20+
- npm or pnpm
- Docker Desktop / Docker Engine
- PostgreSQL client optional

## Setup

```bash
npm install
copy .env.example .env
npm run prisma:generate
docker-compose up -d postgres
npm run prisma:migrate
npm run dev
```

## Useful commands

```bash
npm run build
npm run lint
npm run test
```

## Environment notes

- Frontend API URL defaults to `http://localhost:4000`.
- Database connection uses the `DATABASE_URL` environment variable.
- Secrets must be rotated before production deployment.
