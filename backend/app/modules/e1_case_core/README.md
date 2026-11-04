# E1 · Case management core

**Owner:** Pavan · **Build days:** Day 1–36 · **Tested and signed off by:** Yogendra — Day 40 (Thu 17 Dec)
**Stories:** E1-01 … E1-10 · **Daily tasks:** the "Pavan" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
Create cases, case code, owner, tasks, stage time limits, activity log, checklist gate, exception list, close and revert.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e1_case_core/models.py` | Database tables (columns) |
| `backend/app/modules/e1_case_core/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e1_case_core/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e1_case_core/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e1_case_core/tests/` | One test per "Done when" |
| `frontend/lib/features/e1_case_core/data/` | Dart model + API calls |
| `frontend/lib/features/e1_case_core/screens/` | Full pages |
| `frontend/lib/features/e1_case_core/widgets/` | Small pieces used on your screens |
| `docs/modules/E1-case-core.md` | Your sketches, data plan, decisions |

## What's here now
Empty files with a short note at the top saying what goes in each. Nothing is built yet:
your sheet tasks fill them in, starting with the data plan.

The shared parts you build on are already in place:
- `app/core/database.py`: `Base` and `TimestampMixin` for your tables, `get_db` for endpoints
- `app/core/tenancy.py`: `TenantMixin` and `get_company_id` (company separation)
- `frontend/lib/core/api_client.dart` and `frontend/lib/shared/widgets/states.dart`

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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E1 · Case management core"
pytest app/modules/e1_case_core   # once you have added tests
```

## First tasks from the sheet
- [ ] Day 4: create the case table
- [ ] Day 6: required fields when creating a case
- [ ] Day 7: case from manual entry
