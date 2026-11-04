import 'package:flutter/material.dart';

import '../data/review_request_model.dart';

/// One row in the E4 list. Small, reusable pieces like this go in widgets/.
class ReviewRequestTile extends StatelessWidget {
  const ReviewRequestTile({super.key, required this.item});

  final ReviewRequest item;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const CircleAvatar(child: Text('E4')),
      title: Text(item.doctorName),
      subtitle: Text('case id: ${item.caseId} · status: ${item.status} · expires at: ${item.expiresAt}'),
    );
  }
}
