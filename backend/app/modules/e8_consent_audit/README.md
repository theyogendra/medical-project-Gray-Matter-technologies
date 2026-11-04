# E8 · Consent and audit

**Owner:** Varun · **Build days:** Day 1–36 · **Tested and signed off by:** Yogendra — Day 41 (Fri 18 Dec)
**Stories:** E8-xx (see Varun's tab) · **Daily tasks:** the "Varun" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
Scoped consent, revoke, receipts, server-side access checks, keep period and deletion, access export, support access.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e8_consent_audit/models.py` | Database tables (columns) |
| `backend/app/modules/e8_consent_audit/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e8_consent_audit/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e8_consent_audit/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e8_consent_audit/tests/` | One test per "Done when" |
| `frontend/lib/features/e8_consent_audit/data/` | Dart model + API calls |
| `frontend/lib/features/e8_consent_audit/screens/` | Full pages |
| `frontend/lib/features/e8_consent_audit/widgets/` | Small pieces used on your screens |
| `docs/modules/E8-consent-audit.md` | Your sketches, data plan, decisions |

## Starter code already here
- Table `e8_consents` with columns `case_id`, `scope`, `granted` (plus `id`, `company_id`, `created_at`)
- API: `GET /api/e8/consents`, `POST /api/e8/consents`, `GET /api/e8/consents/{id}`
- `has_consent()` in `service.py` is what other modules (E7, E4) call before sharing anything.
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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E8 · Consent and audit"
pytest app/modules/e8_consent_audit
```

## First tasks from the sheet
- [ ] Day 4: create the consent tables
- [ ] Scoped consent
- [ ] Day 9: confirm screen and privacy notice
