import unittest
from pyboop.main import Boop

class BoopTests(unittest.TestCase):

    def test_place(self):
        newboard = [['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.']]
        boop = Boop()
        self.assertEqual(boop.board, newboard, "board init.")



if __name__ == '__main__':
    unittest.main()