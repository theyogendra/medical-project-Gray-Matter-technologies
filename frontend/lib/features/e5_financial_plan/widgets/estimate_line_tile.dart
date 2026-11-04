import 'package:flutter/material.dart';

import '../data/estimate_line_model.dart';

/// One row in the E5 list. Small, reusable pieces like this go in widgets/.
class EstimateLineTile extends StatelessWidget {
  const EstimateLineTile({super.key, required this.item});

  final EstimateLine item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E5')),
      title: Text(item.groupName),
      subtitle: Text('case id: ${item.caseId} · label: ${item.label} · min amount: ${item.minAmount} · likely amount: ${item.likelyAmount} · certainty: ${item.certainty}'),
    );
  }
}
