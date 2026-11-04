/// E2 · Document — one item returned by GET /api/e2/documents.
///
/// Mirrors `DocumentRead` in backend/app/modules/e2_document_vault/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class Document {
  const Document({
    required this.id,
    required this.caseId,
    required this.fileName,
    required this.docType,
    required this.docDate,
  });

  final int id;
  final int caseId;
  final String fileName;
  final String docType;
  final String docDate;

  /// Builds one Document from the backend's JSON (snake_case keys).
  factory Document.fromJson(Map<String, dynamic> json) => Document(
        id: json['id'] as int,
        caseId: json['case_id'] as int,
        fileName: json['file_name'] as String,
        docType: json['doc_type'] as String,
        docDate: json['doc_date'] as String,
      );
}
