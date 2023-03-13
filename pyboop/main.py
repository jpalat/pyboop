# Import any necessary modules
import sys
import argparse

# Define command-line arguments
parser = argparse.ArgumentParser(description='A program called pyboop')
parser.add_argument('--input', '-i', type=str, required=True, help='The input file for boopy')
parser.add_argument('--output', '-o', type=str, required=True, help='The output file for boopy')

class Boop:
    def __init__(self):
        self.board = [['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.']]

    
    def drawBoard(self):
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print("\n")

# Define the main function
def main(args):
    # TODO: Implement the main functionality of boopy here
    print(f'Running boopy with input file "{args.input}" and output file "{args.output}"')
    boop = Boop()
    boop.drawBoard()

# Call the main function with command-line arguments
if __name__ == '__main__':
    args = parser.parse_args()
    main(args)