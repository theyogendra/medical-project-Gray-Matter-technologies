import '../../../core/api_client.dart';
import 'company_model.dart';

/// Every backend call for E0 · Tenancy and onboarding.
/// Screens call these methods; they never build URLs themselves.
class CompanyApi {
  static const _path = '/api/e0/companies';

  /// GET /api/e0/companies — the list for the current company.
  Future<List<Company>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => Company.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e0/companies — create one. [body] uses the backend's snake_case field names.
  Future<Company> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return Company.fromJson(data);
  }
}
