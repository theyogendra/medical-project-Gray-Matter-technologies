// App-wide settings.

/// Where the backend runs. Override without changing code:
///   flutter run -d chrome --dart-define=API_BASE_URL=http://192.168.1.10:8000
const String apiBaseUrl = String.fromEnvironment(
  'API_BASE_URL',
  defaultValue: 'http://localhost:8000',
);

/// TEMPORARY until E0 builds login: the company we act as (sent as X-Company-Id).
const int devCompanyId = 1;
