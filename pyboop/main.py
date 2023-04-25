# Import any necessary modules
import sys
import argparse

# Define command-line arguments
parser = argparse.ArgumentParser(description='A program called pyboop')
parser.add_argument('--input', '-i', type=str, required=True, help='The input file for boopy')
parser.add_argument('--output', '-o', type=str, required=True, help='The output file for boopy')

class Player:
    def __init__(self):
        self.kittens = 6
        self.cats = 0
    

class Boop:
    def __init__(self, size):
        rows = []
        for i in range(0,size):
            cols = []
            for j in range(0,size):
                cols.append('.')
            rows.append(cols)
        # self.board = [['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.']]
        self.board = rows

    def drawBoard(self):
        print("-------")
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print("\n")

    
    def placeKitten(self, row, col):
        if (x >= 0) and (x < 6) and (y >= 0) and (y < 6):
            if self.board[x][y] == '.':
                self.board[x][y] = 'k'
                self.drawBoard()
                self.kittenboop(x,y)
                return 1
        print("Error placing kitten at", x,y)
        return -1
    
    def kittenboop(self, newx, newy):
        # mutate board with new kitten.
        xpos = [-1,0,1]
        ypos = [-1,0,1]
        for x in xpos:
            for y in ypos:
                if x == 0 and y == 0:
                    print('self')
                    
                else:
                    validation_x = newx + x
                    validation_y = newy + y
                    if self.board[validation_x][validation_y] == 'k':
                        nextvalx = validation_x + x
                        nextvaly = validation_y + y
                        if nextvalx <0 or nextvalx > 6 or nextvaly < 0 or nextvaly > 6:
                            print('out of bounds')
                            self.board[validation_x][validation_y]='.'
                            print("dwb")
                            self.drawBoard()
                        else:
                            if self.board[nextvalx][nextvaly] == 'k':
                               print('two kittens, no move')
                            else: 
                                print('Boop', validation_x, validation_y)
                                self.boop_move(origin_x=validation_x, origin_y=validation_y, off_x=x, off_y=y)

    
    def boop_move(self, origin_x, origin_y, off_x, off_y):
        x = off_x + origin_x
        y = off_y + origin_y
        print ('move: ', origin_x, origin_y, 'to', x, y, 'os', off_x, off_y)
        if x < 0 or x > 6 or y < 0 or y > 6:
            print('return kitten')
        else:
            self.board[x][y] = 'k'
        self.board[origin_x][origin_y] = '.'
        self.drawBoard()
        

                
        

            

# Define the main function
def main(args):
    # TODO: Implement the main functionality of boopy here
    print(f'Running boopy with input file "{args.input}" and output file "{args.output}"')
    boop = Boop(6)
    boop.drawBoard()
    print(boop.board)
    print('place 1,1')
    boop.placeKitten(x=1, y=1)
    print('place 1,2')
    boop.placeKitten(x=1, y=2)
    boop.placeKitten(x=1, y=1)
    boop.placeKitten(x=2, y=2)

# Call the main function with command-line arguments
if __name__ == '__main__':
    args = parser.parse_args()
    main(args)