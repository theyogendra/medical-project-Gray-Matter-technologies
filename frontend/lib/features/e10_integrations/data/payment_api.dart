import '../../../core/api_client.dart';
import 'payment_model.dart';

/// Every backend call for E10 · Integrations.
/// Screens call these methods; they never build URLs themselves.
class PaymentApi {
  static const _path = '/api/e10/payments';

  /// GET /api/e10/payments — the list for the current company.
  Future<List<Payment>> fetchAll() async {
    final data = await ApiClient.instance.get(_path) as List<dynamic>;
    return data.map((e) => Payment.fromJson(e as Map<String, dynamic>)).toList();
  }

  /// POST /api/e10/payments — create one. [body] uses the backend's snake_case field names.
  Future<Payment> create(Map<String, dynamic> body) async {
    final data = await ApiClient.instance.post(_path, body) as Map<String, dynamic>;
    return Payment.fromJson(data);
  }
}
