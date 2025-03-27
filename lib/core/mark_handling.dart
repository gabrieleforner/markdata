class Mark {
  late DateTime markDate;
  late String markSubject;
  late double markValue;

  Mark(DateTime date, String subject, double value) {
    this.markSubject = subject;
    this.markValue = value;
    this.markDate = date;
  }
}

typedef MarksPool = List<Mark>;

double getMeanValue({required List<Mark> values}) {
  if (values.isEmpty) {
    return 0.0;
  }
  return values.map((mark) => mark.markValue).reduce((a, b) => a + b) / values.length;
}
