# medical-project-Gray-Matter-technologies — IPJ-OS

Web application for medical-travel facilitators who bring international patients to India for treatment.

The product is split into **11 modules (E0–E10)**. Each module has **one owner** who builds it end to end
(backend + frontend), and **Yogendra** (lead) tests every module and signs it off.
Day-by-day tasks live in the [team sheet](https://docs.google.com/spreadsheets/d/1jV-3Gq5Xf2UiIezsjQL1AIYd1-KvE572bR3nzeVgIGc/edit).

| Module | Owner | Backend folder | Frontend folder |
| --- | --- | --- | --- |
| E0 · Tenancy and onboarding | Praveen | `backend/app/modules/e0_tenancy/` | `frontend/lib/features/e0_tenancy/` |
| E1 · Case management core | Pavan | `backend/app/modules/e1_case_core/` | `frontend/lib/features/e1_case_core/` |
| E2 · Document vault | Hima Sekhar | `backend/app/modules/e2_document_vault/` | `frontend/lib/features/e2_document_vault/` |
| E3 · Coordinator workspace | Pavan | `backend/app/modules/e3_coordinator_workspace/` | `frontend/lib/features/e3_coordinator_workspace/` |
| E4 · Clinical review | Harshini | `backend/app/modules/e4_clinical_review/` | `frontend/lib/features/e4_clinical_review/` |
| E5 · Treatment financial plan | Harshini | `backend/app/modules/e5_financial_plan/` | `frontend/lib/features/e5_financial_plan/` |
| E6 · Communication timeline | Yogendra | `backend/app/modules/e6_communication/` | `frontend/lib/features/e6_communication/` |
| E7 · Patient journey | Varun | `backend/app/modules/e7_patient_journey/` | `frontend/lib/features/e7_patient_journey/` |
| E8 · Consent and audit | Varun | `backend/app/modules/e8_consent_audit/` | `frontend/lib/features/e8_consent_audit/` |
| E9 · AI layer | Hima Sekhar | `backend/app/modules/e9_ai_layer/` | `frontend/lib/features/e9_ai_layer/` |
| E10 · Integrations | Praveen | `backend/app/modules/e10_integrations/` | `frontend/lib/features/e10_integrations/` |

## How the code is organised

```text
.
├── backend/                 Python API (FastAPI + SQLAlchemy)
│   ├── app/main.py          plugs every module's router into one app
│   ├── app/core/            shared: settings, database, company separation (lead owns)
│   └── app/modules/eN_*/    one folder per module (owner owns)
│        ├── README.md       start here: what the module does and what to build first
│        ├── models.py       database tables
│        ├── schemas.py      shapes of data going in/out of the API
│        ├── service.py      business rules (other modules call these functions)
│        ├── router.py       URLs / endpoints
│        └── tests/          one test per "Done when" in the sheet
├── frontend/                Flutter web app
│   └── lib/
│       ├── main.dart        app start
│       ├── core/            shared: API client, config, home screen, module list (lead owns)
│       ├── shared/widgets/  shared: loading / empty / error states
│       └── features/eN_*/   one folder per module (owner owns)
│            ├── data/       Dart model + API calls
│            ├── screens/    full pages
│            └── widgets/    small reusable pieces
├── docs/                    architecture, conventions, one notes file per module, test plans
└── .github/                 code owners, PR + bug templates, CI checks
```

Every module folder is ready but empty: each file starts with a short note saying what goes in it.
Open your module's `README.md` first, then build it task by task from the sheet.

## Run it on your laptop

### 1. Backend (Python 3.11+)

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate      Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy ..\.env.example .env            # Mac/Linux: cp ../.env.example .env
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs — every module's endpoints are listed there and you can try them.

Run the tests: `pytest` (all modules) or `pytest app/modules/e1_case_core` (one module).

### 2. Frontend (Flutter 3.22+)

```bash
cd frontend
flutter create . --platforms web     # first time only: adds the web/ folder, keeps our code
flutter pub get
flutter run -d chrome
```

The home screen lists all 11 modules. Each shows "Not built yet" until its owner adds a screen.

## How we work together

Read [CONTRIBUTING.md](CONTRIBUTING.md) before your first push. Short version:
branch from `develop` → code only in your module folders → pull request into `develop` → Yogendra reviews and merges.
