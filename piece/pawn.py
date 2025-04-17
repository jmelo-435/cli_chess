from .piece import Piece

class Pawn(Piece):
    
    def to_string(self):
        if self.isWhite():
            return super().to_string()
        return "♟"