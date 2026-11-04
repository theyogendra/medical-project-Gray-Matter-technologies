import '../../../core/api_client.dart';
import 'review_request_model.dart';

/// Every backend call for E4 · Clinical review.
/// Screens call these methods; they never build URLs themselves.
class ReviewRequestApi {
  static const _path = '/api/e4/review-requests';

  /// GET /api/e4/review-requests — the list for the current company.
  Future<List<ReviewRequest>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => ReviewRequest.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e4/review-requests — create one. [body] uses the backend's snake_case field names.
  Future<ReviewRequest> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return ReviewRequest.fromJson(data);
  }
}
