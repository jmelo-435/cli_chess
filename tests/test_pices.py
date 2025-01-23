from ..piece.piece import Piece

piece = Piece()

def test_piece_has_color():
    piece.isWhite() == True

def test_piece_color_is_defined_on_initialization():
    blackPiece = Piece(isWhite=False)
    blackPiece.isWhite() == False