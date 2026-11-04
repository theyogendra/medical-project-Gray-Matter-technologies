import 'package:flutter/material.dart';

import '../../../shared/widgets/states.dart';
import '../data/company_api.dart';
import '../data/company_model.dart';
import '../widgets/company_tile.dart';

/// E0 · Tenancy and onboarding — starter screen (owner: Praveen).
///
/// Shows the list from GET /api/e0/companies with the three required states:
/// loading -> error (with retry) -> empty -> the list.
/// Copy this pattern for your real screens.
class CompanyListScreen extends StatefulWidget {
  const CompanyListScreen({super.key});

  @override
  State<CompanyListScreen> createState() => _CompanyListScreenState();
}

class _CompanyListScreenState extends State<CompanyListScreen> {
  final _api = CompanyApi();
  late Future<List<Company>> _future;

  @override
  void initState() {
    super.initState();
    _future = _api.fetchAll();
  }

  void _reload() {
    setState(() {
      _future = _api.fetchAll();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('E0 · Tenancy and onboarding'),
        actions: [IconButton(onPressed: _reload, icon: const Icon(Icons.refresh))],
      ),
      body: FutureBuilder<List<Company>>(
        future: _future,
        builder: (context, snapshot) {
          if (snapshot.connectionState != ConnectionState.done) {
            return const LoadingState();
          }
          if (snapshot.hasError) {
            return ErrorState(error: snapshot.error!, onRetry: _reload);
          }
          final items = snapshot.data ?? const [];
          if (items.isEmpty) {
            return const EmptyState(message: 'No company found. Is the backend running?');
          }
          return ListView.separated(
            itemCount: items.length,
            separatorBuilder: (context, index) => const Divider(height: 1),
            itemBuilder: (context, index) => CompanyTile(item: items[index]),
          );
        },
      ),
    );
  }
}
