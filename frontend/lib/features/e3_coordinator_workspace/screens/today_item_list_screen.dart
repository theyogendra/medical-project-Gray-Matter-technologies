import 'package:flutter/material.dart';

import '../../../shared/widgets/states.dart';
import '../data/today_item_api.dart';
import '../data/today_item_model.dart';
import '../widgets/today_item_tile.dart';

/// E3 · Coordinator workspace — starter screen (owner: Pavan).
///
/// Shows the list from GET /api/e3/today with the three required states:
/// loading -> error (with retry) -> empty -> the list.
/// Copy this pattern for your real screens.
class TodayItemListScreen extends StatefulWidget {
  const TodayItemListScreen({super.key});

  @override
  State<TodayItemListScreen> createState() => _TodayItemListScreenState();
}

class _TodayItemListScreenState extends State<TodayItemListScreen> {
  final _api = TodayItemApi();
  late Future<List<TodayItem>> _future;

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
        title: const Text('E3 · Coordinator workspace'),
        actions: [IconButton(onPressed: _reload, icon: const Icon(Icons.refresh))],
      ),
      body: FutureBuilder<List<TodayItem>>(
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
            return const EmptyState(message: 'Nothing for today. Add a sample case in E1 first.');
          }
          return ListView.separated(
            itemCount: items.length,
            separatorBuilder: (context, index) => const Divider(height: 1),
            itemBuilder: (context, index) => TodayItemTile(item: items[index]),
          );
        },
      ),
    );
  }
}
