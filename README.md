# Medical Web Application

This repository has been updated to match the finalized technology stack and architecture for the application:

- Frontend: HTML5, CSS3, JavaScript, TypeScript, React.js, Next.js, Tailwind CSS
- Backend: Node.js, Next.js API Routes / Route Handlers, REST APIs
- Database: Supabase PostgreSQL only, Prisma ORM
- Auth: Supabase Auth
- Storage: Supabase Storage
- AI Services: Python + FastAPI + Gemini API

## Architectural update summary

The previous scaffold used a separate NestJS backend and a local PostgreSQL setup. That was corrected to the final stack because the application must use:

1. one Supabase PostgreSQL database only
2. Prisma connected to the existing Supabase PostgreSQL database
3. Next.js for both the web app and the application backend
4. Supabase Auth and Supabase Storage for authentication and files
5. Python + FastAPI as a separate AI service

The original workspace structure was preserved where possible, and the active scaffold was updated in place rather than replaced with a completely unrelated architecture.

## Repository structure

```text
medical-web-application/
├── apps/
│   ├── web/                 # Active Next.js frontend + API backend
│   ├── ai/                  # FastAPI AI service
│   ├── frontend/            # Existing legacy frontend kept for reference
│   └── backend/             # Existing legacy backend kept for reference
├── database/
│   └── prisma/
│       ├── schema.prisma
│       ├── prisma.config.ts
│       └── seed.ts
├── packages/
│   └── shared/
├── docs/
│   ├── architecture/
│   ├── development/
│   └── requirements/
├── .vscode/
│   ├── extensions.json
│   └── settings.json
├── .env.example
├── .gitignore
├── package.json
├── README.md
└── tests/
```

## Important rules implemented

- Only one Supabase PostgreSQL database is used.
- No MongoDB, MySQL, Firebase, or secondary database was introduced.
- Prisma connects to the Supabase PostgreSQL instance through `DATABASE_URL`.
- Next.js hosts both the web UI and API routes.
- FastAPI is isolated for AI service work only.
- Supabase Auth is the default auth layer.
- Supabase Storage is the file and document storage layer.

## Local setup

1. Copy the environment template:
   ```bash
   copy .env.example .env
   ```
2. Fill in your real Supabase and Gemini credentials in `.env`.
3. Install workspace dependencies:
   ```bash
   npm install
   ```
4. Generate Prisma client:
   ```bash
   npm run prisma:generate
   ```
5. Push the schema to Supabase:
   ```bash
   npm run prisma:push
   ```
6. Start the web application:
   ```bash
   npm run dev
   ```
7. Start the AI API service:
   ```bash
   cd apps/ai
   python -m venv .venv
   .venv\Scripts\python -m pip install -r requirements.txt
   .venv\Scripts\python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## VS Code development environment

The workspace includes recommended extensions and settings under `.vscode/` for:

- TypeScript and React tooling
- Tailwind CSS
- Prisma
- Python and FastAPI
- ESLint, Prettier, and debugging support

## Verification status

The foundation work is intentionally limited to scaffold validation and project setup. Business modules remain pending until the scaffold is reviewed and approved.

## Pending approval gate

No full business-module development should begin until the architecture review is approved.
