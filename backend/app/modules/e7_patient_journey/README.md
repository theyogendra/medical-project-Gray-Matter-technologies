# E7 · Patient journey

**Owner:** Varun · **Build days:** Day 37–71 · **Tested and signed off by:** Yogendra — Day 71 (Fri 5 Feb)
**Stories:** E7-xx (see Varun's tab) · **Daily tasks:** the "Varun" tab of the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit)

## What this module does
Family link with one-time code, plain-language stage, phone upload, emergency contact, attendant, slow-network speed, branding.

## Your folders
| Where | What goes there |
| --- | --- |
| `backend/app/modules/e7_patient_journey/models.py` | Database tables (columns) |
| `backend/app/modules/e7_patient_journey/schemas.py` | Shapes of data the API accepts and returns |
| `backend/app/modules/e7_patient_journey/service.py` | Business rules — other modules call these functions |
| `backend/app/modules/e7_patient_journey/router.py` | URLs (endpoints), kept thin |
| `backend/app/modules/e7_patient_journey/tests/` | One test per "Done when" |
| `frontend/lib/features/e7_patient_journey/data/` | Dart model + API calls |
| `frontend/lib/features/e7_patient_journey/screens/` | Full pages |
| `frontend/lib/features/e7_patient_journey/widgets/` | Small pieces used on your screens |
| `docs/modules/E7-patient-journey.md` | Your sketches, data plan, decisions |

## Starter code already here
- Table `e7_family_links` with columns `case_id`, `contact_name`, `phone`, `active` (plus `id`, `company_id`, `created_at`)
- API: `GET /api/e7/family-links`, `POST /api/e7/family-links`, `GET /api/e7/family-links/{id}`
- Extra endpoint `GET /api/e7/journey/{case_id}`: reads the case from E1 and the consent from E8.
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
uvicorn app.main:app --reload      # then open http://localhost:8000/docs -> "E7 · Patient journey"
pytest app/modules/e7_patient_journey
```

## First tasks from the sheet
- [ ] Day 37: sketch the family screens
- [ ] Plan the E7 data
- [ ] Family link with one-time code
