import 'package:flutter/material.dart';

import '../data/company_model.dart';

/// One row in the E0 list. Small, reusable pieces like this go in widgets/.
class CompanyTile extends StatelessWidget {
  const CompanyTile({super.key, required this.item});

  final Company item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E0')),
      title: Text(item.name),
      subtitle: Text('plan: ${item.plan}'),
    );
  }
}
