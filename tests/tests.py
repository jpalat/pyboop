import unittest
import copy
from pyboop.main import Boop

class BoopTests(unittest.TestCase):

    def setUp(self) -> None:
        self.newboard = [['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.']]

    def test_init(self):
        boop = Boop()
        self.assertEqual(boop.board, self.newboard, "board fail.")
    def test_place(self):
        boop = Boop()
        board = copy.deepcopy(self.newboard)
        board[1][1] = 'k'
        boop.placeKitten(x=1, y=1)
        self.assertEqual(boop.board, board, "misplaced kitten")
    def test_place_and_boop(self):
        boop = Boop()
        board = copy.deepcopy(self.newboard) 
        boop.placeKitten(x=1, y=1)
        boop.placeKitten(x=1, y=2)
        board[1][2] = 'k'
        board[1][0] = 'k'
        self.assertEqual(boop.board, board, "moved kitten")
    def test_place_and_boop(self):
        boop = Boop()
        board = copy.deepcopy(self.newboard) 
        boop.placeKitten(x=0, y=1)
        boop.placeKitten(x=1, y=1)
        board[1][1] = 'k'
        self.assertEqual(boop.board, board, "moved kitten")

if __name__ == '__main__':
    unittest.main()