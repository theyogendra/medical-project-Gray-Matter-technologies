/// E9 · Suggestion — one item returned by GET /api/e9/suggestions.
///
/// Mirrors `Suggestion` in backend/app/modules/e9_ai_layer/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class Suggestion {
  const Suggestion({
    required this.documentId,
    required this.fileName,
    required this.currentType,
    required this.suggestedType,
    required this.reason,
  });

  final int documentId;
  final String fileName;
  final String currentType;
  final String suggestedType;
  final String reason;

  /// Builds one Suggestion from the backend's JSON (snake_case keys).
  factory Suggestion.fromJson(Map<String, dynamic> json) => Suggestion(
        documentId: json['document_id'] as int,
        fileName: json['file_name'] as String,
        currentType: json['current_type'] as String,
        suggestedType: json['suggested_type'] as String,
        reason: json['reason'] as String,
      );
}
