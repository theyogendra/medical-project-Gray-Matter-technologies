import 'package:flutter/material.dart';

import 'states.dart';

/// Shown for a module until its owner builds the first real screen.
class ModulePlaceholderScreen extends StatelessWidget {
  const ModulePlaceholderScreen({super.key, required this.code, required this.title});

  final String code;
  final String title;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('$code · $title')),
      body: const EmptyState(message: 'Not built yet. Screens for this module go in its features folder.'),
    );
  }
}
