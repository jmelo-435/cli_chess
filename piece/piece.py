
class Piece():
    _isWhite = True
    coordinates = (0,0)

    def __init__(self,isWhite= True) -> None:
        self._isWhite = isWhite
    
    def isWhite(self):
        return self._isWhite
    
    def moveTo(self,square):
        self.coordinates = square.get_numeral_coordinates()

    def get_coordinates(self):
        return self.coordinates
    
    def to_string(self):
        return "♙"