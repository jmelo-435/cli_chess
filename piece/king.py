from .piece import Piece
from ..utils.coordinates_converter import Converter

class King(Piece):
    def to_string(self):
        if self.is_white():
            return "♔"
        return "♚"
    
    def get_moves(self):
        column = self.coordinates[0]
        file = self.coordinates[1]
        possibilities = []

        for i in range(column-1,column+2):
            for j in range(file-1,file+2):
                if (i,j) != self.coordinates:
                    possibilities.append(Converter().get_alphanumerical_coordinate(i,j))
        
        return  possibilities
        