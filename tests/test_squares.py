from ..square import Square

def test_square_has_coordinates():
    assert Square().get_coordinates() != None

def test_first_square_is_a1():
    assert Square(0,0).get_coordinates() == "a1"

def test_TheSecondSquare_OnFirstColumn_is_a2():
    assert Square(0,1).get_coordinates() == "a2"

def test_TheSeventhSquare_OnFirstColumn_is_a7():
    assert Square(0,6).get_coordinates() == "a7"


