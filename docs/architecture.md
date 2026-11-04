# Architecture

## Big picture

```text
Flutter web app (frontend/)  --HTTP JSON-->  FastAPI backend (backend/)  -->  Database
   one feature folder per module               one module folder per module      SQLite (dev) / PostgreSQL (prod)
```

## Inside a module

```text
screens/  -> data/*_api.dart -> core/api_client.dart  ==HTTP==>  router.py -> service.py -> models.py
```

- **router.py** — URLs only. Reads the request, calls the service, returns the result.
- **service.py** — the rules. The only place that reads/writes the module's tables.
- **models.py** — tables. **schemas.py** — request/response shapes.

## Rules that keep 6 people from breaking each other's work

1. **Own your folders.** Change only your module folders. Shared code (`core/`, `shared/`, `main.py`) goes
   through the lead.
2. **Talk through services.** Module A needs module B's data -> `from app.modules.<b> import service`.
3. **Company separation.** Every company table uses `TenantMixin`; every endpoint uses
   `Depends(get_company_id)`; every query filters by `company_id`. Each module should have a test proving it.
4. **Three screen states.** Loading, empty, error — use `shared/widgets/states.dart`.

## Module dependencies (who calls whom)

| Module | Uses |
| --- | --- |
| E3 Coordinator workspace | E1 cases, later E2, E5, E6 |
| E4 Clinical review | E1 cases, E2 documents, E8 consent |
| E5 Treatment financial plan | E1 cases, E4 opinions |
| E6 Communication timeline | E1 cases, E2 vault (attachments) |
| E7 Patient journey | E1 cases, E8 consent |
| E9 AI layer | E2 documents |
| E10 Integrations | E0 plans (payments), E2 vault (upload checks) |
