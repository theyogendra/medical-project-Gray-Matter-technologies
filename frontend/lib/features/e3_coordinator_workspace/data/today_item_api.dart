import '../../../core/api_client.dart';
import 'today_item_model.dart';

/// Every backend call for E3 · Coordinator workspace.
/// Screens call these methods; they never build URLs themselves.
class TodayItemApi {
  static const _path = '/api/e3/today';

  /// GET /api/e3/today — the list for the current company.
  Future<List<TodayItem>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => TodayItem.fromJson(e as Map<String, dynamic>)).toList();
  }
}
