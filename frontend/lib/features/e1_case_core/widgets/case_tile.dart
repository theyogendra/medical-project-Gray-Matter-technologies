import 'package:flutter/material.dart';

import '../data/case_model.dart';

/// One row in the E1 list. Small, reusable pieces like this go in widgets/.
class CaseTile extends StatelessWidget {
  const CaseTile({super.key, required this.item});

  final Case item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E1')),
      title: Text(item.code),
      subtitle: Text('patient name: ${item.patientName} · country: ${item.country} · stage: ${item.stage} · owner name: ${item.ownerName}'),
    );
  }
}
