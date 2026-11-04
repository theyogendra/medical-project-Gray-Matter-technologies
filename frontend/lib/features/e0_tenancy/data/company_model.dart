/// E0 · Company — one item returned by GET /api/e0/companies.
///
/// Mirrors `CompanyRead` in backend/app/modules/e0_tenancy/schemas.py.
/// When you add a field in the backend, add it here too (and in fromJson).
class Company {
  const Company({
    required this.id,
    required this.name,
    required this.plan,
  });

  final int id;
  final String name;
  final String plan;

  /// Builds one Company from the backend's JSON (snake_case keys).
  factory Company.fromJson(Map<String, dynamic> json) => Company(
        id: json['id'] as int,
        name: json['name'] as String,
        plan: json['plan'] as String,
      );
}
