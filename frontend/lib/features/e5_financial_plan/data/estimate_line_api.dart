import '../../../core/api_client.dart';
import 'estimate_line_model.dart';

/// Every backend call for E5 · Treatment financial plan.
/// Screens call these methods; they never build URLs themselves.
class EstimateLineApi {
  static const _path = '/api/e5/estimate-lines';

  /// GET /api/e5/estimate-lines — the list for the current company.
  Future<List<EstimateLine>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => EstimateLine.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e5/estimate-lines — create one. [body] uses the backend's snake_case field names.
  Future<EstimateLine> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return EstimateLine.fromJson(data);
  }
}
