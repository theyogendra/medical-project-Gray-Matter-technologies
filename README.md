# medical-project-Gray-Matter-technologies — IPJ-OS

Web application for medical-travel facilitators who bring international patients to India for treatment.

The product is split into 11 modules (E0–E10). Each module has one owner who builds it.
Yogendra (lead) reviews every pull request, tests every module and signs it off.

| Person | Branch | Modules |
| --- | --- | --- |
| Yogendra (lead) | `yogendra` | E6 Communication timeline · tests all modules |
| Pavan | `pavan` | E1 Case management core → E3 Coordinator workspace |
| Harshini | `harshini` | E4 Clinical review → E5 Treatment financial plan |
| Praveen | `praveen` | E0 Tenancy and onboarding → E10 Integrations |
| Varun | `varun` | E8 Consent and audit → E7 Patient journey |
| Hima Sekhar | `himasekhar` | E2 Document vault → E9 AI layer |

## How we work

1. Work only on your own branch: `git checkout <your-name>`
2. Before you start each day, get everyone's merged work: `git pull origin main`
3. Write code, then commit with the Story ID first: `git commit -m "E1-01: new case form"`
4. Push your branch: `git push origin <your-name>`
5. Open a pull request from your branch into `main`
6. Yogendra checks it and merges it into `main`

Nobody pushes directly to `main`.
