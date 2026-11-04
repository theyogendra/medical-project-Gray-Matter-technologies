/// E6 · Message — one item returned by GET /api/e6/messages.
///
/// Mirrors `MessageRead` in backend/app/modules/e6_communication/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class Message {
  const Message({
    required this.id,
    required this.caseId,
    required this.channel,
    required this.visibility,
    required this.body,
  });

  final int id;
  final int caseId;
  final String channel;
  final String visibility;
  final String body;

  /// Builds one Message from the backend's JSON (snake_case keys).
  factory Message.fromJson(Map<String, dynamic> json) => Message(
        id: json['id'] as int,
        caseId: json['case_id'] as int,
        channel: json['channel'] as String,
        visibility: json['visibility'] as String,
        body: json['body'] as String,
      );
}
