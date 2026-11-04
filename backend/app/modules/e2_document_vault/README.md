# E2 · Document vault

**Owner:** Hima Sekhar · **Build days:** Day 1–34 · **Tested and signed off by:** Yogendra — Day 38 (Tue 15 Dec)
**Stories:** E2-01 … E2-08 · **Daily tasks:** the "Hima Sekhar" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
Upload documents, keep originals safe, sort, dates, duplicates, missing-documents list, corrections.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e2_document_vault/models.py` | Database tables (columns) |
| `backend/app/modules/e2_document_vault/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e2_document_vault/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e2_document_vault/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e2_document_vault/tests/` | One test per "Done when" |
| `frontend/lib/features/e2_document_vault/data/` | Dart model + API calls |
| `frontend/lib/features/e2_document_vault/screens/` | Full pages |
| `frontend/lib/features/e2_document_vault/widgets/` | Small pieces used on your screens |
| `docs/modules/E2-document-vault.md` | Your sketches, data plan, decisions |

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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E2 · Document vault"
pytest app/modules/e2_document_vault   # once you have added tests
```

## First tasks from the sheet
- [ ] Day 4: private file storage
- [ ] Day 5: create the documents table
- [ ] Day 6: upload a document to a case
