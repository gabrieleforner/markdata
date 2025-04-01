from data.schemas import MarkSchema

def getMean(marks=[MarkSchema]) -> float | None:
    if len(marks) == 0:
        print("No marks to calculate median")
        return None
    sum = 0
    for mark in marks:
        sum += mark.markValue
    return sum / len(marks)

def getTrendingValue(marks):
    """Finds the most frequent markValue (mode) from a list of marks."""

    if not marks: #Check if the list is empty
        return None

    value_counts = {}  # Use a dictionary to count mark values
    for mark in marks:
        value = mark.markValue
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    if not value_counts:
        return None

    most_frequent_value = None
    max_count = 0
    for value, count in value_counts.items():
        if count > max_count:
            most_frequent_value = value
            max_count = count

    return most_frequent_value

def getMedianValue(marks):
    if len(marks) % 2 == 0:
        return len(marks) / 2
    else:
        return (len(marks) + 1) / 2

def getMarksMetrics(marks=[MarkSchema]):
    if len(marks) == 0:
        print("No marks to calculate metrics")
        return
    return