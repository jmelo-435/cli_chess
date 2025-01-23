from ..piece.piece import Piece
from ..board.square import Square

piece = Piece()

def test_piece_has_color():
    piece.isWhite() == True

def test_piece_color_is_defined_on_initialization():
    blackPiece = Piece(isWhite=False)
    blackPiece.isWhite() == False

def test_piece_moves_to_square():
    square = Square()
    piece = Piece()

    piece.moveTo(square)