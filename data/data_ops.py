from datetime import date
from data.schemas import MarkSchema

def addMark(marks=[MarkSchema]):
    try:        
        subjectName    = input("Enter subject name: ")
        markComment = input("Enter comment: ")
        markValue   = float(input("Enter mark value: "))
        markDate    = date.fromisoformat(input("Enter date (YYYY-MM-DD): "))
    except Exception as e:
        print(f"Error: {e}")
        return
    finally:
        marks.append(MarkSchema(subjectName=subjectName, markValue=markValue, markDate=markDate, comment=markComment))
    pass
def removeFromIndex(marks=[MarkSchema]):
    index = int(input("Enter index to remove: "))
    if index < len(marks):
        print(f"confirm to remove mark {marks[index]}?")
        if input("Y/N") == "Y":
            marks.pop(index)
    else:
        print("Index out of range")
    pass