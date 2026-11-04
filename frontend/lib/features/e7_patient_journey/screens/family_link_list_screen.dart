import 'package:flutter/material.dart';

import '../../../shared/widgets/states.dart';
import '../data/family_link_api.dart';
import '../data/family_link_model.dart';
import '../widgets/family_link_tile.dart';

/// E7 · Patient journey — starter screen (owner: Varun).
///
/// Shows the list from GET /api/e7/family-links with the three required states:
/// loading -> error (with retry) -> empty -> the list.
/// Copy this pattern for your real screens.
class FamilyLinkListScreen extends StatefulWidget {
  const FamilyLinkListScreen({super.key});

  @override
  State<FamilyLinkListScreen> createState() => _FamilyLinkListScreenState();
}

class _FamilyLinkListScreenState extends State<FamilyLinkListScreen> {
  final _api = FamilyLinkApi();
  late Future<List<FamilyLink>> _future;

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
        'contact_name': 'Fatima Musa',
        'phone': '+234 800 000 0000',
        'active': true,
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
        title: const Text('E7 · Patient journey'),
        actions: [IconButton(onPressed: _reload, icon: const Icon(Icons.refresh))],
      ),
      body: FutureBuilder<List<FamilyLink>>(
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
            itemBuilder: (context, index) => FamilyLinkTile(item: items[index]),
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
