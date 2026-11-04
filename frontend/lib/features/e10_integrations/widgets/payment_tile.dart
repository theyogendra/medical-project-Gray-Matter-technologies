import 'package:flutter/material.dart';

import '../data/payment_model.dart';

/// One row in the E10 list. Small, reusable pieces like this go in widgets/.
class PaymentTile extends StatelessWidget {
  const PaymentTile({super.key, required this.item});

  final Payment item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E10')),
      title: Text(item.reference),
      subtitle: Text('amount: ${item.amount} · method: ${item.method} · status: ${item.status}'),
    );
  }
}
