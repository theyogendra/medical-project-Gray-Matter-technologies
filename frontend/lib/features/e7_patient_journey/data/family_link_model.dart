/// E7 · FamilyLink — one item returned by GET /api/e7/family-links.
///
/// Mirrors `FamilyLinkRead` in backend/app/modules/e7_patient_journey/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class FamilyLink {
  const FamilyLink({
    required this.id,
    required this.caseId,
    required this.contactName,
    required this.phone,
    required this.active,
  });

  final int id;
  final int caseId;
  final String contactName;
  final String phone;
  final bool active;

  /// Builds one FamilyLink from the backend's JSON (snake_case keys).
  factory FamilyLink.fromJson(Map<String, dynamic> json) => FamilyLink(
        id: json['id'] as int,
        caseId: json['case_id'] as int,
        contactName: json['contact_name'] as String,
        phone: json['phone'] as String,
        active: json['active'] as bool,
      );
}
