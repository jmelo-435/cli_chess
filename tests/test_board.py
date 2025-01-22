from ..board.board import Board

board = Board()

def test_there_is_a_board():
    board = Board()

def test_getSquare_byCoordinate_isPossible():
    assert board.get_square("a1").get_coordinates() == "a1"

def test_getSquare_byCoordinate_returnsRIghtSquare():
    assert board.get_square("a2").get_coordinates() == "a2"

def test_Board_string_Representation():
    f = open("board.txt", "r")
    assert board.toString() == f.read()
    f.close()