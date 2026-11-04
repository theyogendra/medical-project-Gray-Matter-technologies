# E3 · Coordinator workspace

**Owner:** Pavan · **Build days:** Day 37–71 · **Tested and signed off by:** Yogendra — Day 70 (Thu 4 Feb)
**Stories:** E3-01 … E3-06 · **Daily tasks:** the "Pavan" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
Today view, Board view, one-screen case, bulk actions, saved views, speed and keyboard.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e3_coordinator_workspace/models.py` | Database tables (columns) |
| `backend/app/modules/e3_coordinator_workspace/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e3_coordinator_workspace/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e3_coordinator_workspace/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e3_coordinator_workspace/tests/` | One test per "Done when" |
| `frontend/lib/features/e3_coordinator_workspace/data/` | Dart model + API calls |
| `frontend/lib/features/e3_coordinator_workspace/screens/` | Full pages |
| `frontend/lib/features/e3_coordinator_workspace/widgets/` | Small pieces used on your screens |
| `docs/modules/E3-coordinator-workspace.md` | Your sketches, data plan, decisions |

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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E3 · Coordinator workspace"
pytest app/modules/e3_coordinator_workspace   # once you have added tests
```

## First tasks from the sheet
- [ ] Day 37: sketch the workspace screens
- [ ] Day 39: Today view data
- [ ] Day 40: at-risk rule
