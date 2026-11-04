/// E5 · EstimateLine — one item returned by GET /api/e5/estimate-lines.
///
/// Mirrors `EstimateLineRead` in backend/app/modules/e5_financial_plan/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class EstimateLine {
  const EstimateLine({
    required this.id,
    required this.caseId,
    required this.groupName,
    required this.label,
    required this.minAmount,
    required this.likelyAmount,
    required this.certainty,
  });

  final int id;
  final int caseId;
  final String groupName;
  final String label;
  final double minAmount;
  final double likelyAmount;
  final String certainty;

  /// Builds one EstimateLine from the backend's JSON (snake_case keys).
  factory EstimateLine.fromJson(Map<String, dynamic> json) => EstimateLine(
        id: json['id'] as int,
        caseId: json['case_id'] as int,
        groupName: json['group_name'] as String,
        label: json['label'] as String,
        minAmount: (json['min_amount'] as num).toDouble(),
        likelyAmount: (json['likely_amount'] as num).toDouble(),
        certainty: json['certainty'] as String,
      );
}
