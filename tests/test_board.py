from ..board import Board

def test_there_is_a_board():
    board = Board()

def test_getSquare_byCoordinate():
    board = Board()
    assert board.get_square("a1").get_coordinates() == "a1"