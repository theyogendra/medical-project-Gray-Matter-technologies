import 'package:flutter/material.dart';

import '../../../shared/widgets/states.dart';
import '../data/case_api.dart';
import '../data/case_model.dart';
import '../widgets/case_tile.dart';

/// E1 · Case management core — starter screen (owner: Pavan).
///
/// Shows the list from GET /api/e1/cases with the three required states:
/// loading -> error (with retry) -> empty -> the list.
/// Copy this pattern for your real screens.
class CaseListScreen extends StatefulWidget {
  const CaseListScreen({super.key});

  @override
  State<CaseListScreen> createState() => _CaseListScreenState();
}

class _CaseListScreenState extends State<CaseListScreen> {
  final _api = CaseApi();
  late Future<List<Case>> _future;

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

  /// STARTER ONLY: creates a sample row so you can see the full round trip
  /// (screen -> API -> database -> screen). Replace it with your real form.
  Future<void> _addSample() async {
    try {
      await _api.create(<String, dynamic>{
        'code': 'IPJ-0001',
        'patient_name': 'Ahmed Musa',
        'country': 'Nigeria',
        'stage': 'Enquiry',
        'owner_name': 'Coordinator A',
      });
      _reload();
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Could not add: $e')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('E1 · Case management core'),
        actions: [IconButton(onPressed: _reload, icon: const Icon(Icons.refresh))],
      ),
      body: FutureBuilder<List<Case>>(
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
            return const EmptyState(message: 'Nothing here yet. Tap + to add a sample.');
          }
          return ListView.separated(
            itemCount: items.length,
            separatorBuilder: (context, index) => const Divider(height: 1),
            itemBuilder: (context, index) => CaseTile(item: items[index]),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _addSample,
        tooltip: 'Add sample',
        child: const Icon(Icons.add),
      ),
    );
  }
}
