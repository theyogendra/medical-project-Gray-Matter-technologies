# E0 · Tenancy and onboarding — Flutter

Owner: **Praveen**. Full module guide: [`backend/app/modules/e0_tenancy/README.md`](../../../../backend/app/modules/e0_tenancy/README.md)

| Folder | What goes there |
| --- | --- |
| `data/` | Dart classes matching the backend's JSON, and the calls to `/api/e0/...` (through `ApiClient`) |
| `screens/` | Full pages. Each shows loading, empty and error states (`shared/widgets/states.dart`) |
| `widgets/` | Small pieces reused on your screens |

When your first screen exists, point this module's entry in `lib/core/modules.dart` at it (ask the lead to review).
