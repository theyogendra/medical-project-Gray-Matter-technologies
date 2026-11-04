import 'package:flutter/material.dart';

import '../shared/widgets/module_placeholder.dart';

/// One entry per module, shown on the home screen.
/// When a module has its first real screen, its owner passes `builder:` here (lead reviews).
class ModuleInfo {
  const ModuleInfo({
    required this.code,
    required this.title,
    required this.owner,
    this.builder,
  });

  final String code;
  final String title;
  final String owner;

  /// Builds the module's first screen. Null until the module has one.
  final WidgetBuilder? builder;

  /// The screen to open: the real one, or a "not built yet" placeholder.
  Widget open(BuildContext context) =>
      builder?.call(context) ?? ModulePlaceholderScreen(code: code, title: title);
}

const List<ModuleInfo> modules = [
  ModuleInfo(code: 'E0', title: 'Tenancy and onboarding', owner: 'Praveen'),
  ModuleInfo(code: 'E1', title: 'Case management core', owner: 'Pavan'),
  ModuleInfo(code: 'E2', title: 'Document vault', owner: 'Hima Sekhar'),
  ModuleInfo(code: 'E3', title: 'Coordinator workspace', owner: 'Pavan'),
  ModuleInfo(code: 'E4', title: 'Clinical review', owner: 'Harshini'),
  ModuleInfo(code: 'E5', title: 'Treatment financial plan', owner: 'Harshini'),
  ModuleInfo(code: 'E6', title: 'Communication timeline', owner: 'Yogendra'),
  ModuleInfo(code: 'E7', title: 'Patient journey', owner: 'Varun'),
  ModuleInfo(code: 'E8', title: 'Consent and audit', owner: 'Varun'),
  ModuleInfo(code: 'E9', title: 'AI layer', owner: 'Hima Sekhar'),
  ModuleInfo(code: 'E10', title: 'Integrations', owner: 'Praveen'),
];
