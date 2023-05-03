# Import any necessary modules
import sys
import argparse
from enum import Enum

# Define command-line arguments
parser = argparse.ArgumentParser(description='A program called pyboop')
parser.add_argument('--input', '-i', type=str, required=True, help='The input file for boopy')
parser.add_argument('--output', '-o', type=str, required=True, help='The output file for boopy')

class Piece(Enum):
    Player1Kitten = '1'
    Player1Cat = '!'
    Player2Kitten = '2'
    Player2Cat = '@'

    def is_kitten(self):
        if self.value == '1' or self.value =='2':
            return True
        return False
    
    def is_cat(self):
        if self.value == '!' or self.value == '@':
            return True
        return False


class Player:
    def __init__(self):
        self.kittens = 6
        self.cats = 0
    

class Boop:
    def __init__(self, size):
        self.size = size
        rows = []
        for i in range(0,size):
            cols = []
            for j in range(0,size):
                cols.append('.')
            rows.append(cols)
        self.board = rows

    def drawBoard(self):
        print("-------")
        print("  a b c d e f")
        for index, i in enumerate(self.board):
            print(index , end=" ")
            for j in i:
                if isinstance(j,Piece):
                    print(j.value, end=" ")
                else:
                    print(j, end=" ")
            print(index)
        print("  a b c d e f")

    
    def placePiece(self, row, col, type:Piece):
        if (row >= 0) and (row < self.size) and (col >= 0) and (col < self.size):
            if self.board[row][col] == '.':
                self.board[row][col] = type
                self.drawBoard()
                self.boop(row, col, type)
                return 1
        print("Error placing piece at", row,col)
        return -1
    
    def boop(self, newx, newy, type:Piece):
        # mutate board with new Piece.
        xpos = [-1,0,1]
        ypos = [-1,0,1]
        for x in xpos:
            for y in ypos:
                if x == 0 and y == 0:
                    print('self')
                    
                else:
                    validation_x = newx + x
                    validation_y = newy + y
                    if (validation_x >= 0) and (validation_x < self.size) and \
                       (validation_y >= 0) and (validation_y < self.size): 
                        space = self.board[validation_x][validation_y]
                        print('space before eval:', space)
                        if isinstance(space,Piece) and space.is_kitten():
                            nextvalx = validation_x + x
                            nextvaly = validation_y + y
                            if nextvalx <0 or nextvalx > self.size-1 or nextvaly < 0 or nextvaly > self.size-1:
                                print(nextvalx, nextvaly, 'is out of bounds')
                                self.board[validation_x][validation_y]='.'
                            else:
                                next = self.board[nextvalx][nextvaly]
                                if isinstance(next, Piece) and (next.is_kitten() or next.is_cat()):
                                    print('two pieces, no move')
                                else: 
                                    print('Boop', validation_x, validation_y)
                                    self.boop_move(origin_x=validation_x, origin_y=validation_y, off_x=x, off_y=y)
                        else:
                            if isinstance(space, Piece) and space.is_cat():
                                print("Validate Cat", validation_x, validation_y, self.board[validation_x][validation_y], type)
                                if type.is_kitten():
                                    print('No Boop, kittens do not move Cats.', validation_x, validation_y)
                                    continue
                            nextvalx = validation_x + x
                            nextvaly = validation_y + y
                            if nextvalx <0 or nextvalx > self.size-1 or nextvaly < 0 or nextvaly > self.size-1:
                                print('out of bounds, if boop, return to inventory!!!')
                                self.board[validation_x][validation_y]='.'
                            else:
                                next = self.board[nextvalx][nextvaly]
                                print('in the else: ', next)
                                if isinstance(type, Piece) and type.is_cat():
                                    if isinstance(next, Piece): 
                                        if next.is_kitten() or next.is_cat():
                                            print('two pieces, no move')
                                    else: 
                                        print('Boop - cat to cat', validation_x, validation_y)
                                        self.boop_move(origin_x=validation_x, origin_y=validation_y, off_x=x, off_y=y)                                

                    else:
                        print('validation off board')

    
    def boop_move(self, origin_x, origin_y, off_x, off_y):
        x = off_x + origin_x
        y = off_y + origin_y
        print ('move: ', origin_x, origin_y, 'to', x, y, 'os', off_x, off_y)
        if x < 0 or x > self.size or y < 0 or y > self.size:
            print('return kitten')
        else:
            self.board[x][y] = self.board[origin_x][origin_y]
        self.board[origin_x][origin_y] = '.'
        self.drawBoard()
        

                
        

            

# Define the main function
def main(args):
    # TODO: Implement the main functionality of boopy here
    print(f'Running boopy with input file "{args.input}" and output file "{args.output}"')
    boop = Boop(6)
    boop.drawBoard()


# Call the main function with command-line arguments
if __name__ == '__main__':
    args = parser.parse_args()
    main(args)