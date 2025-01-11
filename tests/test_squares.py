from ..square import Square,InvalidSquareException
import pytest

def test_square_has_coordinates():
    assert Square().get_coordinates() != None

def test_first_square_is_a1():
    assert Square(0,0).get_coordinates() == "a1"

def test_TheSecondSquare_OnFirstColumn_is_a2():
    assert Square(0,1).get_coordinates() == "a2"

def test_TheSeventhSquare_OnFirstColumn_is_a7():
    assert Square(0,6).get_coordinates() == "a7"

def test_TheSeventhSquare_OnSecondColumn_is_b7():
    assert Square(1,6).get_coordinates() == "b7"

def test_TheSeventhSquare_OnSeventhColumn_is_g7():
    assert Square(6,6).get_coordinates() == "g7"

def test_a1_isBlack():
    assert Square(0,0).isBlack() ==  True

def test_b1_is_Not_Black():
    assert Square(1,0).isBlack() ==  False

def test_a1c1e1g1_isBlack():
    assert Square(0,0).isBlack() ==  True
    assert Square(2,0).isBlack() ==  True
    assert Square(4,0).isBlack() ==  True
    assert Square(6,0).isBlack() ==  True

def test_ColumnNumberAboveMax_ThrowsException():
    with pytest.raises(InvalidSquareException):
        Square(8,6)

def test_RowNumberAboveMax_ThrowsException():
    with pytest.raises(InvalidSquareException):
        Square(6,8)
