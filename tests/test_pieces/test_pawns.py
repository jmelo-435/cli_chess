from ...piece.pawn import Pawn
from ...board.square import Square
pawn = Pawn()

def test_pawn_has_color():
    assert pawn.isWhite()==True

def test_pawn_to_string():
    assert pawn.to_string() == "♙"

def test_string_representation_for_black_pawns():
    black_pawn = Pawn(isWhite=False)
    assert black_pawn.to_string() == "♟"

def test_pawn_moves():
    square = Square(1,1)
    pawn = Pawn()
    pawn.moveTo(square=square)
    assert pawn.get_moves() == ["b3"]

def test_pawn_moves_acceptance():
    square = Square(5,6)
    pawn = Pawn()
    pawn.moveTo(square=square)
    assert pawn.get_moves() == ["f8"]