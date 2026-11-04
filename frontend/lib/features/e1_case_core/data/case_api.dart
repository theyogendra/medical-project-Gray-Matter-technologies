import '../../../core/api_client.dart';
import 'case_model.dart';

/// Every backend call for E1 · Case management core.
/// Screens call these methods; they never build URLs themselves.
class CaseApi {
  static const _path = '/api/e1/cases';

  /// GET /api/e1/cases — the list for the current company.
  Future<List<Case>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => Case.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e1/cases — create one. [body] uses the backend's snake_case field names.
  Future<Case> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return Case.fromJson(data);
  }
}
