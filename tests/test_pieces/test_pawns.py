from ...piece.pawn import Pawn

pawn = Pawn()

def test_pawn_has_color():
    assert pawn.isWhite()==True

def test_pawn_to_string():
    assert pawn.to_string() == "♙"

def test_string_representation_for_black_pawns():
    black_pawn = Pawn(isWhite=False)
    assert black_pawn.to_string() == "♟"
