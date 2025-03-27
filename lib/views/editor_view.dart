import 'package:fl_chart/fl_chart.dart';
import 'package:markdata/core/mark_handling.dart';
import 'package:flutter/material.dart';

class EditorView extends StatefulWidget {
  const EditorView({super.key});

  @override
  State<StatefulWidget> createState() => EditorViewState();
}

class EditorViewState extends State<EditorView> {
  // The marksPool is set to late due to
  // later updating both by user or by a file opening
  late MarksPool marksPool;
  double meanMarkValue = 0;

  // UI Controllers
  final subjectTfController = TextEditingController();
  final markValueTfController = TextEditingController();
  // final dateTfController = TextEditingController();

  @override
  void dispose() {
    super.dispose();
    // dateTfController.dispose();
    subjectTfController.dispose();
    markValueTfController.dispose();
  }

  @override
  void initState() {
    super.initState();
    marksPool = [];
  }

  // UI main
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Center(
          child: Column(
            children: [
              // Marks inout row
              Row(
                children: [
                  SizedBox(
                    width: 400,
                    child: TextField(
                      controller: subjectTfController,
                      decoration: InputDecoration(
                        labelText: 'Subject Name',
                        border: OutlineInputBorder(),
                      ),
                    ),
                  ),
                  SizedBox(width: 8.0),
                  SizedBox(
                    width: 200,
                    child: TextField(
                      controller: markValueTfController,
                      decoration: InputDecoration(
                        labelText: 'Mark Value',
                        border: OutlineInputBorder(),
                      ),
                    ),
                  ),

                  TextButton(
                    onPressed: () {
                      setState(() {
                        if (markValueTfController.text.isEmpty ||
                            markValueTfController.text.contains(
                              RegExp(r'[^\d.]'),
                            )) {
                          showDialog(
                            context: context,
                            builder: (BuildContext context) {
                              return AlertDialog(
                                title: Text("Invalid data!"),
                                content: Text(
                                  "Mark value cannot be empty or contain letters/symbols!",
                                ),
                                actions: [
                                  TextButton(
                                    onPressed: () {
                                      Navigator.of(context).pop();
                                    },
                                    child: Text("OK"),
                                  ),
                                ],
                              );
                            },
                          );
                        } else {
                          marksPool.add(
                            Mark(
                              DateTime(2023),
                              subjectTfController.text.isEmpty
                                  ? "<unknown>"
                                  : subjectTfController.text,
                              double.tryParse(markValueTfController.text) ??
                                  0.0,
                            ),
                          );
                          // Invalidate old mean value and recompute
                          meanMarkValue = 0;
                          meanMarkValue = getMeanValue(values: marksPool);
                          markValueTfController.clear();
                          subjectTfController.clear();
                        }
                      });
                    },
                    child: Text("Add"),
                  ),
                ],
              ),
              // Marks table & graph
              if (marksPool.isEmpty)
                Padding(
                  padding: EdgeInsets.all(250),
                  child: Center(child: Text("No marks present!")),
                )
              else
                Row(
                  children: [
                    Padding(
                      padding: EdgeInsets.all(20.0),
                      child: DataTable(
                        columns: [
                          DataColumn(label: Text("Subject")),
                          DataColumn(label: Text("Mark")),
                          DataColumn(label: Text("Remove Option")),
                        ],
                        rows: [
                          ...marksPool.map((markEntry) {
                            final subject = markEntry.markSubject;
                            final mark = markEntry.markValue;
                            return DataRow(
                              cells: [
                                DataCell(Text(subject)),
                                DataCell(Text(mark.toString())),
                                DataCell(
                                  TextButton(
                                    onPressed: () {
                                      setState(() {
                                        marksPool.remove(markEntry);
                                        meanMarkValue = 0;
                                        meanMarkValue = getMeanValue(
                                          values: marksPool,
                                        );
                                      });
                                    },
                                    child: Text("Remove"),
                                  ),
                                ),
                              ],
                            );
                          }),
                        ],
                      ),
                    ),
                    Spacer(),
                    Column(
                      children: [
                        // TODO: Chart for beatiful cose
                        Text(
                          "Mean value: $meanMarkValue",
                          style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                    Spacer(),
                  ],
                ),
            ],
          ),
        ),
      ),
    );
  }
}
