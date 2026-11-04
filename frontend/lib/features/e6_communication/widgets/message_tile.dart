import 'package:flutter/material.dart';

import '../data/message_model.dart';

/// One row in the E6 list. Small, reusable pieces like this go in widgets/.
class MessageTile extends StatelessWidget {
  const MessageTile({super.key, required this.item});

  final Message item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E6')),
      title: Text(item.channel),
      subtitle: Text('case id: ${item.caseId} · visibility: ${item.visibility} · body: ${item.body}'),
    );
  }
}
