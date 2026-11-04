import '../../../core/api_client.dart';
import 'suggestion_model.dart';

/// Every backend call for E9 · AI layer.
/// Screens call these methods; they never build URLs themselves.
class SuggestionApi {
  static const _path = '/api/e9/suggestions';

  /// GET /api/e9/suggestions — the list for the current company.
  Future<List<Suggestion>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => Suggestion.fromJson(e as Map<String, dynamic>)).toList();
  }
}
