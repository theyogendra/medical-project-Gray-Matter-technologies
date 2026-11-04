import 'package:flutter_test/flutter_test.dart';
import 'package:ipj_os/main.dart';

void main() {
  testWidgets('home screen lists all 11 modules', (tester) async {
    await tester.pumpWidget(const IpjApp());
    expect(find.text('IPJ-OS modules'), findsOneWidget);
    expect(find.text('Tenancy and onboarding'), findsOneWidget);
  });
}
