import 'package:flutter/material.dart';

import '../data/suggestion_model.dart';

/// One row in the E9 list. Small, reusable pieces like this go in widgets/.
class SuggestionTile extends StatelessWidget {
  const SuggestionTile({super.key, required this.item});

  final Suggestion item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E9')),
      title: Text(item.fileName),
      subtitle: Text('document id: ${item.documentId} · current type: ${item.currentType} · suggested type: ${item.suggestedType} · reason: ${item.reason}'),
    );
  }
}
