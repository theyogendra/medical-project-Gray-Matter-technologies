import 'package:flutter/material.dart';

import '../../../shared/widgets/states.dart';
import '../data/estimate_line_api.dart';
import '../data/estimate_line_model.dart';
import '../widgets/estimate_line_tile.dart';

/// E5 · Treatment financial plan — starter screen (owner: Harshini).
///
/// Shows the list from GET /api/e5/estimate-lines with the three required states:
/// loading -> error (with retry) -> empty -> the list.
/// Copy this pattern for your real screens.
class EstimateLineListScreen extends StatefulWidget {
  const EstimateLineListScreen({super.key});

  @override
  State<EstimateLineListScreen> createState() => _EstimateLineListScreenState();
}

class _EstimateLineListScreenState extends State<EstimateLineListScreen> {
  final _api = EstimateLineApi();
  late Future<List<EstimateLine>> _future;

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
        'group_name': 'Hospital',
        'label': 'Surgery package',
        'min_amount': 250000.0,
        'likely_amount': 300000.0,
        'certainty': 'Likely',
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
        title: const Text('E5 · Treatment financial plan'),
        actions: [IconButton(onPressed: _reload, icon: const Icon(Icons.refresh))],
      ),
      body: FutureBuilder<List<EstimateLine>>(
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
            itemBuilder: (context, index) => EstimateLineTile(item: items[index]),
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
