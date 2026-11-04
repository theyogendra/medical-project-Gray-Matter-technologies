import 'package:flutter/material.dart';

import 'core/home_screen.dart';

/// App start. Keep this file tiny: theme + first screen only.
void main() {
  runApp(const IpjApp());
}

class IpjApp extends StatelessWidget {
  const IpjApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'IPJ-OS',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(colorSchemeSeed: const Color(0xFF0F766E), useMaterial3: true),
      home: const HomeScreen(),
    );
  }
}
