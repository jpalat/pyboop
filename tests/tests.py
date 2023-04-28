import unittest
import copy
from pyboop.main import Boop, Piece

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
        board[1][1] = Piece.Kitten
        boop.placePiece(row=1, col=1, type=Piece.Kitten)
        self.assertEqual(boop.board, board, "misplaced kitten")

    def test_place_small(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                    ['.', '.', '.'], 
                    ['.', '.', '.']]
        board[0][2] = Piece.Kitten
        boop.placePiece(row=0, col=2, type=Piece.Kitten)
        self.assertEqual(boop.board, board, "misplaced kitten")

    def test_place_and_boop(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=1, col=1, type=Piece.Kitten)
        boop.placePiece(row=0, col =1, type=Piece.Kitten)
        board[0][1] = Piece.Kitten
        board[2][1] = Piece.Kitten
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_and_boop_cat(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=1, col=1, type=Piece.Cat)
        boop.placePiece(row=0, col =1, type=Piece.Cat)
        board[0][1] = Piece.Cat
        board[2][1] = Piece.Cat
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_and_kitten_cat_noboop(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=1, col=1, type=Piece.Cat)
        boop.placePiece(row=0, col =1, type=Piece.Kitten)
        board[0][1] = Piece.Kitten
        board[1][1] = Piece.Cat
        self.assertEqual(boop.board, board, "failed to boop kitten")


    def test_place_with_edge_left(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=1, type=Piece.Kitten)
        boop.placePiece(row=1, col=1, type=Piece.Kitten)
        board[1][1] = Piece.Kitten
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_with_edge_cardinal(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=1, type=Piece.Kitten)
        boop.placePiece(row=1, col=0, type=Piece.Kitten)
        boop.placePiece(row=1, col=2, type=Piece.Kitten)
        boop.placePiece(row=2, col=1, type=Piece.Kitten)
        boop.placePiece(row=1, col=1, type=Piece.Kitten)
        board[1][1] = Piece.Kitten
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_with_edge_corners(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=0, type=Piece.Kitten)
        boop.placePiece(row=0, col=2, type=Piece.Kitten)
        boop.placePiece(row=2, col=0, type=Piece.Kitten)
        boop.placePiece(row=2, col=2, type=Piece.Kitten)
        boop.placePiece(row=1, col=1, type=Piece.Kitten)
        board[1][1] = Piece.Kitten
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_two_kitten(self):
        boop = Boop(6)
        board = [['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.']]
        boop.placePiece(row=1, col=1, type=Piece.Kitten)
        boop.placePiece(row=1, col=3, type=Piece.Kitten)
        boop.placePiece(row=1, col=4, type=Piece.Kitten)
        boop.placePiece(row=1, col=3, type=Piece.Kitten)
        board[1][1] = Piece.Kitten
        board[1][2] = Piece.Kitten
        board[1][3] = Piece.Kitten
        board[1][5] = Piece.Kitten
        self.assertEqual(boop.board, board, "two kittens fail")

    def test_place_Cat_with_edge_corners(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=0, type=Piece.Kitten)
        boop.placePiece(row=0, col=2, type=Piece.Kitten)
        boop.placePiece(row=2, col=0, type=Piece.Kitten)
        boop.placePiece(row=2, col=2, type=Piece.Kitten)
        boop.placePiece(row=1, col=1, type=Piece.Cat)
        board[1][1] = Piece.Cat
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_Cat_with_Cats_edge_corners(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=0, type=Piece.Cat)
        boop.placePiece(row=0, col=2, type=Piece.Cat)
        boop.placePiece(row=2, col=0, type=Piece.Cat)
        boop.placePiece(row=2, col=2, type=Piece.Cat)
        boop.placePiece(row=1, col=1, type=Piece.Cat)
        board[1][1] = Piece.Cat
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_kitten_with_Cats_edge_corners(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=0, type=Piece.Cat)
        boop.placePiece(row=0, col=2, type=Piece.Cat)
        boop.placePiece(row=2, col=0, type=Piece.Cat)
        boop.placePiece(row=2, col=2, type=Piece.Cat)
        boop.placePiece(row=1, col=1, type=Piece.Kitten)
        board[1][1] = Piece.Kitten
        board[0][0] = Piece.Cat
        board[0][2] = Piece.Cat
        board[2][0] = Piece.Cat
        board[2][2] = Piece.Cat
        boop.drawBoard()
        self.assertEqual(boop.board, board, "failed to boop kitten")

if __name__ == '__main__':
    unittest.main()