
class Piece():
    _isWhite = True
    coordinates = (0,0)

    def __init__(self,isWhite= True) -> None:
        self._isWhite = isWhite
    
    def is_white(self):
        return self._isWhite
    
    def move_to(self,square):
        self.coordinates = square.get_numeral_coordinates()

    def get_coordinates(self):
        return self.coordinates
    
    def to_string(self):
        return "♙"