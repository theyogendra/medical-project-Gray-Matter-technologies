import 'package:flutter/material.dart';

import '../../../shared/widgets/states.dart';
import '../data/suggestion_api.dart';
import '../data/suggestion_model.dart';
import '../widgets/suggestion_tile.dart';

/// E9 · AI layer — starter screen (owner: Hima Sekhar).
///
/// Shows the list from GET /api/e9/suggestions with the three required states:
/// loading -> error (with retry) -> empty -> the list.
/// Copy this pattern for your real screens.
class SuggestionListScreen extends StatefulWidget {
  const SuggestionListScreen({super.key});

  @override
  State<SuggestionListScreen> createState() => _SuggestionListScreenState();
}

class _SuggestionListScreenState extends State<SuggestionListScreen> {
  final _api = SuggestionApi();
  late Future<List<Suggestion>> _future;

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
        title: const Text('E9 · AI layer'),
        actions: [IconButton(onPressed: _reload, icon: const Icon(Icons.refresh))],
      ),
      body: FutureBuilder<List<Suggestion>>(
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
            return const EmptyState(message: 'No suggestions. Add a document in E2 with a wrong type, e.g. \'blood_report.pdf\' typed as \'Other\'.');
          }
          return ListView.separated(
            itemCount: items.length,
            separatorBuilder: (context, index) => const Divider(height: 1),
            itemBuilder: (context, index) => SuggestionTile(item: items[index]),
          );
        },
      ),
    );
  }
}
