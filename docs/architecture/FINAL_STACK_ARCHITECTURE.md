# Finalized architecture update

## Objective

This document captures the corrected architecture for the medical application after the original scaffold was reviewed against the finalized technology stack.

## Final technology stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| Frontend | HTML5, CSS3, JavaScript, TypeScript, React.js, Next.js, Tailwind CSS | App UI and user experience |
| Application backend | Next.js API routes / route handlers | Core backend logic, REST endpoints, server-side API behavior |
| Database | Supabase PostgreSQL | Single source of truth for application data |
| ORM | Prisma | Type-safe database access and schema management |
| Auth | Supabase Auth | Secure user authentication |
| Storage | Supabase Storage | File and document storage |
| AI layer | Python + FastAPI + Gemini API | AI inference and document analysis services |

## Key corrections applied

1. Replaced the separate NestJS backend with Next.js as the main application backend.
2. Kept Prisma but pointed it at the Supabase PostgreSQL instance instead of a local database-only setup.
3. Removed the assumption of local JWT-only auth and replaced it with Supabase Auth.
4. Kept FastAPI as a separate AI service instead of mixing it into the main web stack.
5. Preserved the original monorepo structure while making the active scaffold consistent with the final stack.

## Folder purpose

- `apps/web`: active Next.js application for the frontend, API routes, and app backend
- `apps/ai`: Python FastAPI AI service
- `database/prisma`: shared Prisma schema, migration config, and seed files
- `packages/shared`: reusable application contracts and shared logic
- `.vscode`: workspace-level settings and recommended extensions
- `docs`: product, architecture, and operational documentation

## Important configuration files

- `apps/web/package.json`: Next.js project scripts and dependency definitions
- `apps/web/tsconfig.json`: TypeScript compiler config for Next.js
- `apps/web/tailwind.config.ts`: Tailwind CSS setup and theme extensions
- `apps/web/next.config.mjs`: Next.js runtime configuration
- `database/prisma/schema.prisma`: Prisma schema used with Supabase PostgreSQL
- `.env.example`: template for all required environment variables
- `apps/ai/requirements.txt`: Python dependency list for the AI service

## Deployment and runtime guidance

- The application should run against a single Supabase PostgreSQL instance.
- Supabase Auth is the authentication provider.
- Supabase Storage is used for files, documents, and uploads.
- The AI service remains separate and does not replace the main app backend.

## Review gate

Business module development remains blocked until this scaffold is reviewed and approved.
