# Folder Structure

```text
medical-web-application/
├── apps/
│   ├── frontend/
│   │   ├── src/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── vite.config.ts
│   │   └── tailwind.config.js
│   └── backend/
│       ├── src/
│       ├── package.json
│       ├── nest-cli.json
│       └── tsconfig.json
├── database/
│   └── prisma/
│       ├── schema.prisma
│       └── seed.ts
├── docs/
│   ├── PROJECT_OVERVIEW.md
│   ├── FOLDER_STRUCTURE.md
│   ├── requirements/
│   ├── architecture/
│   ├── database/
│   ├── api/
│   ├── authentication/
│   ├── roles/
│   ├── development/
│   ├── testing/
│   └── deployment/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── package.json
├── README.md
└── tests/
```

## Intent

- `apps/frontend`: UI foundation, layout, routes, auth, API layer
- `apps/backend`: NestJS API, Prisma integration, auth logic, role-based foundation
- `database/prisma`: central schema and seed data
- `docs`: architecture and requirements documentation
- `tests`: future integration and end-to-end coverage
