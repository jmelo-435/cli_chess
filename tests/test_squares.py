from ..square import Square

def test_square_has_coordinates():
    assert Square().get_coordinates() != None

def test_first_square_is_a1():
    assert Square(0,0).get_coordinates() == "a1"


