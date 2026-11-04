/// E8 · Consent — one item returned by GET /api/e8/consents.
///
/// Mirrors `ConsentRead` in backend/app/modules/e8_consent_audit/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class Consent {
  const Consent({
    required this.id,
    required this.caseId,
    required this.scope,
    required this.granted,
  });

  final int id;
  final int caseId;
  final String scope;
  final bool granted;

  /// Builds one Consent from the backend's JSON (snake_case keys).
  factory Consent.fromJson(Map<String, dynamic> json) => Consent(
        id: json['id'] as int,
        caseId: json['case_id'] as int,
        scope: json['scope'] as String,
        granted: json['granted'] as bool,
      );
}
