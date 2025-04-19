from ...piece.king import King
from ...board.square import Square


king = King()

def test_king_has_color():
    assert king.is_white() == True

def test_king_to_string():
    assert king.to_string() == "♔"

def test_string_representation_for_black_king():
    black_king = King(isWhite=False)
    assert black_king.to_string() == "♚"

def test_king_moves():
    square = Square(1,1)
    king = King()
    king.move_to(square=square)
    assert king.get_moves().sort() == ["b3","a3","c3","a2","c2","b1","a1","c1"].sort()