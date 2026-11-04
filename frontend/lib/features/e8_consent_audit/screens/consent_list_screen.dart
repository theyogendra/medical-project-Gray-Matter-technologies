import 'package:flutter/material.dart';

import '../../../shared/widgets/states.dart';
import '../data/consent_api.dart';
import '../data/consent_model.dart';
import '../widgets/consent_tile.dart';

/// E8 · Consent and audit — starter screen (owner: Varun).
///
/// Shows the list from GET /api/e8/consents with the three required states:
/// loading -> error (with retry) -> empty -> the list.
/// Copy this pattern for your real screens.
class ConsentListScreen extends StatefulWidget {
  const ConsentListScreen({super.key});

  @override
  State<ConsentListScreen> createState() => _ConsentListScreenState();
}

class _ConsentListScreenState extends State<ConsentListScreen> {
  final _api = ConsentApi();
  late Future<List<Consent>> _future;

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
        'case_id': 1,
        'scope': 'Share reports with Dr. Rao',
        'granted': true,
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
        title: const Text('E8 · Consent and audit'),
        actions: [IconButton(onPressed: _reload, icon: const Icon(Icons.refresh))],
      ),
      body: FutureBuilder<List<Consent>>(
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
            itemBuilder: (context, index) => ConsentTile(item: items[index]),
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
