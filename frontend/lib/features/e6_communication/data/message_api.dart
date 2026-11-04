import '../../../core/api_client.dart';
import 'message_model.dart';

/// Every backend call for E6 · Communication timeline.
/// Screens call these methods; they never build URLs themselves.
class MessageApi {
  static const _path = '/api/e6/messages';

  /// GET /api/e6/messages — the list for the current company.
  Future<List<Message>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => Message.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e6/messages — create one. [body] uses the backend's snake_case field names.
  Future<Message> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return Message.fromJson(data);
  }
}
