import 'package:flutter/material.dart';

import '../data/family_link_model.dart';

/// One row in the E7 list. Small, reusable pieces like this go in widgets/.
class FamilyLinkTile extends StatelessWidget {
  const FamilyLinkTile({super.key, required this.item});

  final FamilyLink item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E7')),
      title: Text(item.contactName),
      subtitle: Text('case id: ${item.caseId} · phone: ${item.phone} · active: ${item.active}'),
    );
  }
}
