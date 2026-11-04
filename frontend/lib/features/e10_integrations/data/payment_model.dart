/// E10 · Payment — one item returned by GET /api/e10/payments.
///
/// Mirrors `PaymentRead` in backend/app/modules/e10_integrations/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class Payment {
  const Payment({
    required this.id,
    required this.amount,
    required this.method,
    required this.status,
    required this.reference,
  });

  final int id;
  final double amount;
  final String method;
  final String status;
  final String reference;

  /// Builds one Payment from the backend's JSON (snake_case keys).
  factory Payment.fromJson(Map<String, dynamic> json) => Payment(
        id: json['id'] as int,
        amount: (json['amount'] as num).toDouble(),
        method: json['method'] as String,
        status: json['status'] as String,
        reference: json['reference'] as String,
      );
}
