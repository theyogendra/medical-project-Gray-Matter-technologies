import '../../../core/api_client.dart';
import 'document_model.dart';

/// Every backend call for E2 · Document vault.
/// Screens call these methods; they never build URLs themselves.
class DocumentApi {
  static const _path = '/api/e2/documents';

  /// GET /api/e2/documents — the list for the current company.
  Future<List<Document>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => Document.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e2/documents — create one. [body] uses the backend's snake_case field names.
  Future<Document> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return Document.fromJson(data);
  }
}
