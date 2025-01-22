from .square import Square

class Board():
    squares = []

    def __init__(self) -> None:
        i=0
        while i <8:
            j=0
            while j <8:
                self.squares.append(Square(i,j))
                j += 1
            i+=1

    def get_square(self,coordinate):
        
        return next(square for square in self.squares if square.get_coordinates() == coordinate)  
    
    def _add_foot_coordinates(self,board):
        footer = "     a       b       c       d       e       f       g       h    "
        return board + footer

    def toString(self):
        i = 0
        representation = ""

        while i<8:
            k=0
            while k <4:
                if k ==0:
                    representation += (str(8-i)+" ")
                else:
                    representation += ("  ")
                j = 0
                while j<8:
                    square = next(square for square in self.squares if square.get_numeral_coordinates() == (j,i))
                    representation += square.print()
                    j+=1
                k+=1
            i+=1
        
        return self._add_foot_coordinates(representation)

        
    