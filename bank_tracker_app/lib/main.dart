import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const BankTrackerApp());
}

class BankTrackerApp extends StatelessWidget {
  const BankTrackerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bank Tracker',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF6C63FF),
        ),
        useMaterial3: true,
      ),
      home: const HomeScreen(),
    );
  }
}
