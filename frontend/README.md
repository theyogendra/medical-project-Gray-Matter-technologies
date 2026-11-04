# IPJ-OS frontend (Flutter web)

```bash
flutter create . --platforms web   # first time only: adds web/ and keeps our lib/ code
flutter pub get
flutter run -d chrome              # backend must be running on http://localhost:8000
```

Different backend address? `flutter run -d chrome --dart-define=API_BASE_URL=http://192.168.1.10:8000`

## Folders

| Folder | What | Owner |
| --- | --- | --- |
| `lib/main.dart` | App start | Lead |
| `lib/core/` | Config, API client, module list, home screen | Lead |
| `lib/shared/widgets/` | Loading / empty / error widgets every screen uses | Lead |
| `lib/features/eN_*/data/` | That module's Dart model + API calls | Module owner |
| `lib/features/eN_*/screens/` | That module's pages | Module owner |
| `lib/features/eN_*/widgets/` | Small pieces used on that module's pages | Module owner |

Rules: screens never build URLs or call `http` directly — they call their module's `data/*_api.dart`,
which calls `ApiClient`. Every screen shows loading, empty and error states (use `shared/widgets/states.dart`).
