import 'package:flutter/material.dart';

import 'modules.dart';

/// Development home screen: one tile per module, so every teammate can open
/// their own module. The real navigation comes later (E3 workspace, E7 family app).
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('IPJ-OS modules')),
      body: ListView.separated(
        itemCount: modules.length,
        separatorBuilder: (context, index) => const Divider(height: 1),
        itemBuilder: (context, index) {
          final module = modules[index];
          return ListTile(
            leading: CircleAvatar(child: Text(module.code)),
            title: Text(module.title),
            subtitle: Text('Owner: ${module.owner}'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => Navigator.of(context).push(MaterialPageRoute(builder: module.open)),
          );
        },
      ),
    );
  }
}
