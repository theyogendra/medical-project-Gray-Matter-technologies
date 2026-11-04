import 'package:flutter/material.dart';

import '../data/document_model.dart';

/// One row in the E2 list. Small, reusable pieces like this go in widgets/.
class DocumentTile extends StatelessWidget {
  const DocumentTile({super.key, required this.item});

  final Document item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E2')),
      title: Text(item.fileName),
      subtitle: Text('case id: ${item.caseId} · doc type: ${item.docType} · doc date: ${item.docDate}'),
    );
  }
}
