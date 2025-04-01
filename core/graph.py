from data.schemas import MarkSchema
from matplotlib import pyplot as plt
from matplotlib import use
from numpy import array

def plotMarksGraph(marksArray=None):
    if len(marksArray) == 0:
        print("No marks to plot")
        return
    plt.xlabel("Time")
    plt.ylabel("Marks")
    sortedMarks = sorted(marksArray, key=lambda mark: mark.markDate)
    plt.plot(
        array([mark.markDate for mark in sortedMarks]),
        array([mark.markValue for mark in sortedMarks]),
    )
    plt.show()
    pass