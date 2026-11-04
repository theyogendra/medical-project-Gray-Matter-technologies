# E4 · Clinical review

**Owner:** Harshini · **Build days:** Day 1–36 · **Tested and signed off by:** Yogendra — Day 39 (Wed 16 Dec)
**Stories:** E4-01 … E4-06 · **Daily tasks:** the "Harshini" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
Secure doctor review links, doctor opinion form, request more info, compare opinions.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e4_clinical_review/models.py` | Database tables (columns) |
| `backend/app/modules/e4_clinical_review/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e4_clinical_review/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e4_clinical_review/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e4_clinical_review/tests/` | One test per "Done when" |
| `frontend/lib/features/e4_clinical_review/data/` | Dart model + API calls |
| `frontend/lib/features/e4_clinical_review/screens/` | Full pages |
| `frontend/lib/features/e4_clinical_review/widgets/` | Small pieces used on your screens |
| `docs/modules/E4-clinical-review.md` | Your sketches, data plan, decisions |

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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E4 · Clinical review"
pytest app/modules/e4_clinical_review   # once you have added tests
```

## First tasks from the sheet
- [ ] Day 4: create review request and opinion tables
- [ ] Day 5: doctor list for the company
- [ ] Day 6: secure review link with expiry
