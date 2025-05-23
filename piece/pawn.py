from .piece import Piece
from ..utils.coordinates_converter import Converter

class Pawn(Piece):
    
    def to_string(self):
        if self.is_white():
            return super().to_string()
        return "♟"
    
    def get_moves(self):
        current_column = self.get_coordinates()[0]
        current_file = self.get_coordinates()[1]
        return [Converter().get_alphanumerical_coordinate(current_file+1,current_column)]
