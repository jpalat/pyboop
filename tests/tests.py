import unittest
import copy
from pyboop.main import Boop

class BoopTests(unittest.TestCase):

    # def setUp(self):
    #     print("tests set")

    def test_init(self):
        boop = Boop(6)
        newboard = [['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.']]
        
        self.assertEqual(boop.board, newboard, "board fail.")
    def test_size(self):
        boop = Boop(3)
        newboard = [['.', '.', '.'], 
                    ['.', '.', '.'], 
                    ['.', '.', '.']]
        self.assertEqual(boop.board, newboard, "board fail.")
    def test_place(self):
        boop = Boop(6)
        board = [['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.']]
        board[1][1] = 'k'
        boop.placeKitten(x=1, y=1)
        self.assertEqual(boop.board, board, "misplaced kitten")
    def test_place_small(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                    ['.', '.', '.'], 
                    ['.', '.', '.']]
        board[1][1] = 'k'
        boop.placeKitten(x=1, y=1)
        self.assertEqual(boop.board, board, "misplaced kitten")
    def test_place_and_boop(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placeKitten(x=1, y=1)
        boop.placeKitten(x=0, y=1)
        board[0][1] = 'k'
        board[2][1] = 'k'
        self.assertEqual(boop.board, board, "failed to boop kitten")
    def test_place_with_edge(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placeKitten(x=0, y=1)
        boop.placeKitten(x=1, y=1)
        board[1][1] = 'k'
        self.assertEqual(boop.board, board, "failed to boop kitten")

if __name__ == '__main__':
    unittest.main()