import unittest
import copy
from pyboop.main import Boop

class BoopTests(unittest.TestCase):

    def setUp(self):
        print("tests set")

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
        boop.placeKitten(row=1, col=1)
        self.assertEqual(boop.board, board, "misplaced kitten")
    def test_place_small(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                    ['.', '.', '.'], 
                    ['.', '.', '.']]
        board[0][2] = 'k'
        boop.placeKitten(row=0, col=2)
        self.assertEqual(boop.board, board, "misplaced kitten")
    def test_place_and_boop(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placeKitten(row=1, col=1)
        boop.placeKitten(row=0, col =1)
        board[0][1] = 'k'
        board[2][1] = 'k'
        self.assertEqual(boop.board, board, "failed to boop kitten")
    def test_place_with_edge_left(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placeKitten(row=0, col=1)
        boop.placeKitten(row=1, col=1)
        board[1][1] = 'k'
        self.assertEqual(boop.board, board, "failed to boop kitten")
    def test_place_with_edge_cardinal(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placeKitten(row=0, col=1)
        boop.placeKitten(row=1, col=0)
        boop.placeKitten(row=1, col=2)
        boop.placeKitten(row=2, col=1)
        boop.placeKitten(row=1, col=1)
        board[1][1] = 'k'
        self.assertEqual(boop.board, board, "failed to boop kitten")
    def test_place_with_edge_corners(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placeKitten(row=0, col=0)
        boop.placeKitten(row=0, col=2)
        boop.placeKitten(row=2, col=0)
        boop.placeKitten(row=2, col=2)
        boop.placeKitten(row=1, col=1)
        board[1][1] = 'k'
        self.assertEqual(boop.board, board, "failed to boop kitten")

if __name__ == '__main__':
    unittest.main()