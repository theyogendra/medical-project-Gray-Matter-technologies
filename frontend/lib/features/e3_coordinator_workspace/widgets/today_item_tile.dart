import 'package:flutter/material.dart';

import '../data/today_item_model.dart';

/// One row in the E3 list. Small, reusable pieces like this go in widgets/.
class TodayItemTile extends StatelessWidget {
  const TodayItemTile({super.key, required this.item});

  final TodayItem item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E3')),
      title: Text(item.patientName),
      subtitle: Text('case id: ${item.caseId} · code: ${item.code} · stage: ${item.stage} · next action: ${item.nextAction}'),
    );
  }
}
