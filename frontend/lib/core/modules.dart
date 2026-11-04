import 'package:flutter/material.dart';

import '../features/e0_tenancy/screens/company_list_screen.dart';
import '../features/e1_case_core/screens/case_list_screen.dart';
import '../features/e2_document_vault/screens/document_list_screen.dart';
import '../features/e3_coordinator_workspace/screens/today_item_list_screen.dart';
import '../features/e4_clinical_review/screens/review_request_list_screen.dart';
import '../features/e5_financial_plan/screens/estimate_line_list_screen.dart';
import '../features/e6_communication/screens/message_list_screen.dart';
import '../features/e7_patient_journey/screens/family_link_list_screen.dart';
import '../features/e8_consent_audit/screens/consent_list_screen.dart';
import '../features/e9_ai_layer/screens/suggestion_list_screen.dart';
import '../features/e10_integrations/screens/payment_list_screen.dart';

/// One entry per module, shown on the home screen.
/// Adding a module here is a shared-code change (lead reviews).
class ModuleInfo {
  const ModuleInfo({
    required this.code,
    required this.title,
    required this.owner,
    required this.builder,
  });

  final String code;
  final String title;
  final String owner;

  /// Builds the module's first screen.
  final WidgetBuilder builder;
}

final List<ModuleInfo> modules = [
  ModuleInfo(
    code: 'E0',
    title: 'Tenancy and onboarding',
    owner: 'Praveen',
    builder: (context) => const CompanyListScreen(),
  ),
  ModuleInfo(
    code: 'E1',
    title: 'Case management core',
    owner: 'Pavan',
    builder: (context) => const CaseListScreen(),
  ),
  ModuleInfo(
    code: 'E2',
    title: 'Document vault',
    owner: 'Hima Sekhar',
    builder: (context) => const DocumentListScreen(),
  ),
  ModuleInfo(
    code: 'E3',
    title: 'Coordinator workspace',
    owner: 'Pavan',
    builder: (context) => const TodayItemListScreen(),
  ),
  ModuleInfo(
    code: 'E4',
    title: 'Clinical review',
    owner: 'Harshini',
    builder: (context) => const ReviewRequestListScreen(),
  ),
  ModuleInfo(
    code: 'E5',
    title: 'Treatment financial plan',
    owner: 'Harshini',
    builder: (context) => const EstimateLineListScreen(),
  ),
  ModuleInfo(
    code: 'E6',
    title: 'Communication timeline',
    owner: 'Yogendra',
    builder: (context) => const MessageListScreen(),
  ),
  ModuleInfo(
    code: 'E7',
    title: 'Patient journey',
    owner: 'Varun',
    builder: (context) => const FamilyLinkListScreen(),
  ),
  ModuleInfo(
    code: 'E8',
    title: 'Consent and audit',
    owner: 'Varun',
    builder: (context) => const ConsentListScreen(),
  ),
  ModuleInfo(
    code: 'E9',
    title: 'AI layer',
    owner: 'Hima Sekhar',
    builder: (context) => const SuggestionListScreen(),
  ),
  ModuleInfo(
    code: 'E10',
    title: 'Integrations',
    owner: 'Praveen',
    builder: (context) => const PaymentListScreen(),
  ),
];
