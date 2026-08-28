import 'package:flutter/material.dart';

void main() {
  runApp(const AccidentAlertApp());
}

class AccidentAlertApp extends StatelessWidget {
  const AccidentAlertApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Accident Alert System',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.red,
        ),
        useMaterial3: true,
      ),
      home: const AccidentHomePage(),
    );
  }
}

class AccidentHomePage extends StatelessWidget {
  const AccidentHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Accident Alert System',
        ),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment:
                MainAxisAlignment.center,
            children: [

              const Icon(
                Icons.car_crash,
                size: 90,
                color: Colors.red,
              ),

              const SizedBox(height: 25),

              const Text(
                'Accident Detection System',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
                textAlign: TextAlign.center,
              ),

              const SizedBox(height: 20),

              const Text(
                'Waiting for accident information...',
                style: TextStyle(
                  fontSize: 18,
                ),
                textAlign: TextAlign.center,
              ),

              const SizedBox(height: 30),

              ElevatedButton(
                onPressed: () {

                  ScaffoldMessenger.of(context)
                      .showSnackBar(
                    const SnackBar(
                      content: Text(
                        'No accident detected.',
                      ),
                    ),
                  );

                },
                child: const Text(
                  'Check Status',
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
