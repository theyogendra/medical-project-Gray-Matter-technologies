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

## Starter code already here
- Table `e2_documents` with columns `case_id`, `file_name`, `doc_type`, `doc_date` (plus `id`, `company_id`, `created_at`)
- API: `GET /api/e2/documents`, `POST /api/e2/documents`, `GET /api/e2/documents/{id}`
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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E2 · Document vault"
pytest app/modules/e2_document_vault
```

## First tasks from the sheet
- [ ] Day 4: private file storage
- [ ] Day 5: create the documents table
- [ ] Day 6: upload a document to a case
