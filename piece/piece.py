
class Piece():
    _isWhite = True

    def __init__(self,isWhite= True) -> None:
        self._isWhite = isWhite
    
    def isWhite(self):
        return self._isWhite