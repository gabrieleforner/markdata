from numpy import array

from core.cli import cli_main
from data.schemas import MarkSchema

marksArray = [  ]

def main():
    print(f"MarkData v0.1-dev")
    cli_main(marksArray=marksArray)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl-C Hit! Exiting...")