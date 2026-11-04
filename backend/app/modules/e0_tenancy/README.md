# E0 · Tenancy and onboarding

**Owner:** Praveen · **Build days:** Day 1–34 · **Tested and signed off by:** Yogendra — Day 37 (Mon 14 Dec)
**Stories:** E0-01 … E0-08 · **Daily tasks:** the "Praveen" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
Sign-up, company account, plans, payment, settings, first run, data export.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e0_tenancy/models.py` | Database tables (columns) |
| `backend/app/modules/e0_tenancy/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e0_tenancy/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e0_tenancy/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e0_tenancy/tests/` | One test per "Done when" |
| `frontend/lib/features/e0_tenancy/data/` | Dart model + API calls |
| `frontend/lib/features/e0_tenancy/screens/` | Full pages |
| `frontend/lib/features/e0_tenancy/widgets/` | Small pieces used on your screens |
| `docs/modules/E0-tenancy.md` | Your sketches, data plan, decisions |

## Starter code already here
- Table `e0_companies` with columns `name`, `plan`
- API: `GET /api/e0/companies`, `GET /api/e0/companies/me`, `POST /api/e0/companies`
- `ensure_demo_company()` creates company #1 when the server starts
- Tests: create + list, get one, **company separation**, missing fields refused
- Flutter: a list screen with loading / empty / error states

The starter code is an **example of the pattern**, not the final design. Rename and change the fields
to match the data plan Yogendra approves.

## How one request flows through your code

```text
Flutter screen (screens/)
   -> data/*_api.dart          builds the URL, calls ApiClient
   -> core/api_client.dart     adds headers, sends HTTP
   -> router.py                checks the request, calls service
   -> service.py               business rules, filtered by company_id
   -> models.py                the database table
```

## Run just your module

```bash
cd backend
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E0 · Tenancy and onboarding"
pytest app/modules/e0_tenancy
```

## First tasks from the sheet
- [ ] Day 4: create the company and user tables
- [ ] Day 5: keep each company's data separate
- [ ] Day 7: sign-up with email and verification
