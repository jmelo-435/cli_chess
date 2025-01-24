from ..piece.piece import Piece
from ..board.square import Square

def test_piece_moves_to_square():
    square = Square()
    piece = Piece()

    piece.moveTo(square)    

def test_piece_AfterMovingToASquare_HasTheRightCoordinate():
    square = Square()
    piece = Piece()

    piece.moveTo(square)
    assert piece.get_coordinates()==(0,0)


def test_piece_AfterMovingToASquare_HasTheCoordinateOfLastSquare():
    square = Square()
    second_square = Square(1,1)
    piece = Piece()

    piece.moveTo(square)
    piece.moveTo(second_square)
    assert piece.get_coordinates()==(1,1)