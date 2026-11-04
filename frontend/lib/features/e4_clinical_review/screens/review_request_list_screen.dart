import 'package:flutter/material.dart';

import '../../../shared/widgets/states.dart';
import '../data/review_request_api.dart';
import '../data/review_request_model.dart';
import '../widgets/review_request_tile.dart';

/// E4 · Clinical review — starter screen (owner: Harshini).
///
/// Shows the list from GET /api/e4/review-requests with the three required states:
/// loading -> error (with retry) -> empty -> the list.
/// Copy this pattern for your real screens.
class ReviewRequestListScreen extends StatefulWidget {
  const ReviewRequestListScreen({super.key});

  @override
  State<ReviewRequestListScreen> createState() => _ReviewRequestListScreenState();
}

class _ReviewRequestListScreenState extends State<ReviewRequestListScreen> {
  final _api = ReviewRequestApi();
  late Future<List<ReviewRequest>> _future;

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
        'doctor_name': 'Dr. Rao',
        'status': 'Sent',
        'expires_at': '2026-11-10',
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
        title: const Text('E4 · Clinical review'),
        actions: [IconButton(onPressed: _reload, icon: const Icon(Icons.refresh))],
      ),
      body: FutureBuilder<List<ReviewRequest>>(
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
            itemBuilder: (context, index) => ReviewRequestTile(item: items[index]),
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
