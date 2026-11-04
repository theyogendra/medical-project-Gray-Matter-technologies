import 'dart:convert';

import 'package:http/http.dart' as http;

import 'config.dart';

/// The ONE place that talks HTTP to the backend.
///
/// Feature code never uses `http` directly. When E0 adds login, only this file
/// changes (to send the login token) and every module keeps working.
class ApiClient {
  ApiClient._();

  /// Use `ApiClient.instance` everywhere.
  static final ApiClient instance = ApiClient._();

  Map<String, String> get _headers => {
        'Content-Type': 'application/json',
        'X-Company-Id': '$devCompanyId',
      };

  /// GET [path] (e.g. '/api/e1/cases') and return the decoded JSON.
  Future<dynamic> get(String path) async {
    final response = await http.get(Uri.parse('$apiBaseUrl$path'), headers: _headers);
    return _decode(response);
  }

  /// POST [body] as JSON to [path] and return the decoded JSON reply.
  Future<dynamic> post(String path, Map<String, dynamic> body) async {
    final response = await http.post(
      Uri.parse('$apiBaseUrl$path'),
      headers: _headers,
      body: jsonEncode(body),
    );
    return _decode(response);
  }

  dynamic _decode(http.Response response) {
    if (response.statusCode >= 200 && response.statusCode < 300) {
      return jsonDecode(response.body);
    }
    throw ApiException(response.statusCode, response.body);
  }
}

/// Thrown when the backend answers with an error (4xx / 5xx).
class ApiException implements Exception {
  ApiException(this.statusCode, this.body);

  final int statusCode;
  final String body;

  @override
  String toString() => 'API error $statusCode: $body';
}
