from core.graph import plotMarksGraph
from data.data_ops import addMark, removeFromIndex
from data.metrics import getMarksMetrics


commands = {
    'exit': lambda _: exit(),
    'clear' : lambda _: print("\033[H\033[J"),
    'view': lambda marksArray: print("\n".join([f"i={i}, {marksArray[i]}" for i in range(len(marksArray))]) if marksArray else "No marks to view"),
    'add' : lambda marksArray: addMark(marksArray),
    'remove' : lambda marksArray: removeFromIndex(marksArray),
    'get-metrics' : lambda marksArray: getMarksMetrics(marksArray),
    'get-graph'   : lambda marksArray: plotMarksGraph(marksArray),
#    'load-json'   : lambda marksArray: print("Not implemented yet"),   TODO: Need to document on this for deseriaize
#    'save-json'   : lambda marksArray: print("Not implemented yet"),   TODO: Need to document on this for serialize
}

def cli_main(marksArray=None):
    while True:
        line = input("(markdata): ")
        command = line.split(' ')
        if command[0] in commands:
            commands[command[0]](marksArray)
        elif command[0] == '':
            pass
        else:
            print(f"Unknown command: {command[0]}")
