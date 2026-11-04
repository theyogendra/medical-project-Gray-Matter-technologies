import '../../../core/api_client.dart';
import 'family_link_model.dart';

/// Every backend call for E7 · Patient journey.
/// Screens call these methods; they never build URLs themselves.
class FamilyLinkApi {
  static const _path = '/api/e7/family-links';

  /// GET /api/e7/family-links — the list for the current company.
  Future<List<FamilyLink>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => FamilyLink.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e7/family-links — create one. [body] uses the backend's snake_case field names.
  Future<FamilyLink> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return FamilyLink.fromJson(data);
  }
}
