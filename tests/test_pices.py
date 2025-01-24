from ..piece.piece import Piece

piece = Piece()

def test_piece_has_color():
    assert piece.isWhite() == True

def test_piece_color_is_defined_on_initialization():
    blackPiece = Piece(isWhite=False)
    assert blackPiece.isWhite() == False

def test_piece_to_string():
    assert piece.to_string() == "♙"