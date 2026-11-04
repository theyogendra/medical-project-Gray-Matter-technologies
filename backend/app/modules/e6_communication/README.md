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

## Starter code already here
- Table `e6_messages` with columns `case_id`, `channel`, `visibility`, `body` (plus `id`, `company_id`, `created_at`)
- API: `GET /api/e6/messages`, `POST /api/e6/messages`, `GET /api/e6/messages/{id}`
- Tests: create + list, get one, **company separation**, missing fields refused
- Flutter: a list screen with an **Add sample** button with loading / empty / error states

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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E6 · Communication timeline"
pytest app/modules/e6_communication
```

## First tasks from the sheet
- [ ] Day 14: plan the E6 data
- [ ] Create the message table
- [ ] Timeline list
