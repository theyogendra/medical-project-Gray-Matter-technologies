import 'package:flutter/material.dart';

import '../data/consent_model.dart';

/// One row in the E8 list. Small, reusable pieces like this go in widgets/.
class ConsentTile extends StatelessWidget {
  const ConsentTile({super.key, required this.item});

  final Consent item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E8')),
      title: Text(item.scope),
      subtitle: Text('case id: ${item.caseId} · granted: ${item.granted}'),
    );
  }
}
