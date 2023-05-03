import unittest
import copy
from pyboop.main import Boop, Piece

class BoopTests(unittest.TestCase):



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
        board[1][1] = Piece.Player1Kitten
        boop.placePiece(row=1, col=1, type=Piece.Player1Kitten)
        self.assertEqual(boop.board, board, "misplaced kitten")

    def test_place_small(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                    ['.', '.', '.'], 
                    ['.', '.', '.']]
        board[0][2] = Piece.Player1Kitten
        boop.placePiece(row=0, col=2, type=Piece.Player1Kitten)
        self.assertEqual(boop.board, board, "misplaced kitten")

    def test_place_and_boop(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=1, col=1, type=Piece.Player1Kitten)
        boop.placePiece(row=0, col =1, type=Piece.Player1Kitten)
        board[0][1] = Piece.Player1Kitten
        board[2][1] = Piece.Player1Kitten
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_and_boop_cat(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=1, col=1, type=Piece.Player1Cat)
        boop.placePiece(row=0, col =1, type=Piece.Player2Cat)
        board[0][1] = Piece.Player2Cat
        board[2][1] = Piece.Player1Cat
        self.assertEqual(boop.board, board, "test_place_and_boop_cat")

    def test_place_and_kitten_cat_noboop(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]

        boop.placePiece(row=1, col=1, type=Piece.Player2Cat)
        boop.placePiece(row=0, col=1, type=Piece.Player1Kitten)
        board[1][1] = Piece.Player2Cat
        board[0][1] = Piece.Player1Kitten
        print("State before test")
        boop.drawBoard()
        self.assertEqual(boop.board, board, "FAIL: kitten booped a cat")


    def test_place_with_edge_left(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=1, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=1, type=Piece.Player1Kitten)
        board[1][1] = Piece.Player1Kitten
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_with_edge_cardinal(self):
        boop = Boop(3)
        boop.drawBoard()
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=1, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=0, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=2, type=Piece.Player1Kitten)
        boop.placePiece(row=2, col=1, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=1, type=Piece.Player1Kitten)
        board[1][1] = Piece.Player1Kitten
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_with_edge_corners(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=0, type=Piece.Player1Kitten)
        boop.placePiece(row=0, col=2, type=Piece.Player1Kitten)
        boop.placePiece(row=2, col=0, type=Piece.Player1Kitten)
        boop.placePiece(row=2, col=2, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=1, type=Piece.Player1Kitten)
        board[1][1] = Piece.Player1Kitten
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_two_kitten(self):
        boop = Boop(6)
        board = [['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.'], 
                    ['.', '.', '.', '.', '.', '.']]
        boop.placePiece(row=1, col=1, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=3, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=4, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=3, type=Piece.Player1Kitten)
        board[1][1] = Piece.Player1Kitten
        board[1][2] = Piece.Player1Kitten
        board[1][3] = Piece.Player1Kitten
        board[1][5] = Piece.Player1Kitten
        self.assertEqual(boop.board, board, "two kittens fail")

    def test_place_Cat_with_edge_corners(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=0, type=Piece.Player1Kitten)
        boop.placePiece(row=0, col=2, type=Piece.Player1Kitten)
        boop.placePiece(row=2, col=0, type=Piece.Player1Kitten)
        boop.placePiece(row=2, col=2, type=Piece.Player1Kitten)
        boop.placePiece(row=1, col=1, type=Piece.Player2Cat)
        board[1][1] = Piece.Player2Cat
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_Cat_with_Cats_edge_corners(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=0, type=Piece.Player2Cat)
        boop.placePiece(row=0, col=2, type=Piece.Player2Cat)
        boop.placePiece(row=2, col=0, type=Piece.Player2Cat)
        boop.placePiece(row=2, col=2, type=Piece.Player2Cat)
        boop.placePiece(row=1, col=1, type=Piece.Player1Cat)
        board[1][1] = Piece.Player1Cat
        self.assertEqual(boop.board, board, "failed to boop kitten")

    def test_place_kitten_with_Cats_edge_corners(self):
        boop = Boop(3)
        board = [['.', '.', '.'], 
                 ['.', '.', '.'],
                 ['.', '.', '.']]
        boop.placePiece(row=0, col=0, type=Piece.Player2Cat)
        boop.placePiece(row=0, col=2, type=Piece.Player2Cat)
        boop.placePiece(row=2, col=0, type=Piece.Player2Cat)
        boop.placePiece(row=2, col=2, type=Piece.Player2Cat)
        boop.placePiece(row=1, col=1, type=Piece.Player1Kitten)
        board[1][1] = Piece.Player1Kitten
        board[0][0] = Piece.Player2Cat
        board[0][2] = Piece.Player2Cat
        board[2][0] = Piece.Player2Cat
        board[2][2] = Piece.Player2Cat
        boop.drawBoard()
        self.assertEqual(boop.board, board, "failed to boop kitten")

if __name__ == '__main__':
    unittest.main()