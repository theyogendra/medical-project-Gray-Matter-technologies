/// E4 · ReviewRequest — one item returned by GET /api/e4/review-requests.
///
/// Mirrors `ReviewRequestRead` in backend/app/modules/e4_clinical_review/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class ReviewRequest {
  const ReviewRequest({
    required this.id,
    required this.caseId,
    required this.doctorName,
    required this.status,
    required this.expiresAt,
  });

  final int id;
  final int caseId;
  final String doctorName;
  final String status;
  final String expiresAt;

  /// Builds one ReviewRequest from the backend's JSON (snake_case keys).
  factory ReviewRequest.fromJson(Map<String, dynamic> json) => ReviewRequest(
        id: json['id'] as int,
        caseId: json['case_id'] as int,
        doctorName: json['doctor_name'] as String,
        status: json['status'] as String,
        expiresAt: json['expires_at'] as String,
      );
}
