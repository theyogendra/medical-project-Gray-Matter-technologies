# E6 · Communication timeline

**Owner:** Yogendra · **Build days:** Day 14–66 · **Tested and signed off by:** Yogendra — Final check Day 66 with Pavan
**Stories:** E6-xx (see Yogendra's tab) · **Daily tasks:** the "Yogendra" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
One timeline of every message (in-app, email, WhatsApp), Patient-visible / Internal-only / Clinical labels, 15 templates, attachments into the vault.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e6_communication/models.py` | Database tables (columns) |
| `backend/app/modules/e6_communication/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e6_communication/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e6_communication/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e6_communication/tests/` | One test per "Done when" |
| `frontend/lib/features/e6_communication/data/` | Dart model + API calls |
| `frontend/lib/features/e6_communication/screens/` | Full pages |
| `frontend/lib/features/e6_communication/widgets/` | Small pieces used on your screens |
| `docs/modules/E6-communication.md` | Your sketches, data plan, decisions |

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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E6 · Communication timeline"
pytest app/modules/e6_communication   # once you have added tests
```

## First tasks from the sheet
- [ ] Day 14: plan the E6 data
- [ ] Create the message table
- [ ] Timeline list
