import '../../../core/api_client.dart';
import 'consent_model.dart';

/// Every backend call for E8 · Consent and audit.
/// Screens call these methods; they never build URLs themselves.
class ConsentApi {
  static const _path = '/api/e8/consents';

  /// GET /api/e8/consents — the list for the current company.
  Future<List<Consent>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => Consent.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e8/consents — create one. [body] uses the backend's snake_case field names.
  Future<Consent> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return Consent.fromJson(data);
  }
}
