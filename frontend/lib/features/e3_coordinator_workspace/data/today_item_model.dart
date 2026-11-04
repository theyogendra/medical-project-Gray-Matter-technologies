/// E3 · TodayItem — one item returned by GET /api/e3/today.
///
/// Mirrors `TodayItem` in backend/app/modules/e3_coordinator_workspace/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class TodayItem {
  const TodayItem({
    required this.caseId,
    required this.code,
    required this.patientName,
    required this.stage,
    required this.nextAction,
  });

  final int caseId;
  final String code;
  final String patientName;
  final String stage;
  final String nextAction;

  /// Builds one TodayItem from the backend's JSON (snake_case keys).
  factory TodayItem.fromJson(Map<String, dynamic> json) => TodayItem(
        caseId: json['case_id'] as int,
        code: json['code'] as String,
        patientName: json['patient_name'] as String,
        stage: json['stage'] as String,
        nextAction: json['next_action'] as String,
      );
}
