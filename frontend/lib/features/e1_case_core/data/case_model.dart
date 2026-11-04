/// E1 · Case — one item returned by GET /api/e1/cases.
///
/// Mirrors `CaseRead` in backend/app/modules/e1_case_core/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class Case {
  const Case({
    required this.id,
    required this.code,
    required this.patientName,
    required this.country,
    required this.stage,
    required this.ownerName,
  });

  final int id;
  final String code;
  final String patientName;
  final String country;
  final String stage;
  final String ownerName;

  /// Builds one Case from the backend's JSON (snake_case keys).
  factory Case.fromJson(Map<String, dynamic> json) => Case(
        id: json['id'] as int,
        code: json['code'] as String,
        patientName: json['patient_name'] as String,
        country: json['country'] as String,
        stage: json['stage'] as String,
        ownerName: json['owner_name'] as String,
      );
}
