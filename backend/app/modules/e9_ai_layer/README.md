# E9 · AI layer

**Owner:** Hima Sekhar · **Build days:** Day 35–71 · **Tested and signed off by:** Yogendra — Day 68 (Tue 2 Feb)
**Stories:** E9-xx (see Hima Sekhar's tab) · **Daily tasks:** the "Hima Sekhar" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
AI sorting and dates, sourced case summary, missing-documents check, next-step navigator, safety rules.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e9_ai_layer/models.py` | Database tables (columns) |
| `backend/app/modules/e9_ai_layer/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e9_ai_layer/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e9_ai_layer/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e9_ai_layer/tests/` | One test per "Done when" |
| `frontend/lib/features/e9_ai_layer/data/` | Dart model + API calls |
| `frontend/lib/features/e9_ai_layer/screens/` | Full pages |
| `frontend/lib/features/e9_ai_layer/widgets/` | Small pieces used on your screens |
| `docs/modules/E9-ai-layer.md` | Your sketches, data plan, decisions |

## Starter code already here
- No table of its own yet; it builds `Suggestion` rows (`document_id`, `file_name`, `current_type`, `suggested_type`, `reason`) from another module (see `service.py`).
- API: `GET /api/e9/suggestions`
- Rule-based placeholder for AI sorting: reads documents through `e2_document_vault.service` and always returns a `reason` (AI answers must show their source).
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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E9 · AI layer"
pytest app/modules/e9_ai_layer
```

## First tasks from the sheet
- [ ] Day 35: plan the AI data and safety rules
- [ ] AI sorting of document types
- [ ] Sourced case summary
