# Testing Strategy

## Foundation coverage

- Unit tests for auth and app service logic.
- Integration test scaffolding for the API layer.
- Database validation through Prisma and migrations.
- Frontend component smoke tests for route and auth shell.

## Tools

- Jest for backend tests.
- Vitest for frontend tests.
- Playwright for end-to-end smoke coverage when feature work begins.

## Minimum quality gates

- Application builds successfully.
- Linting runs without blocking errors.
- Automated tests pass in the foundation setup.
- Prisma schema validates cleanly.
