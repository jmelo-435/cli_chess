from .square import Square

class Board():
    squares = []
    _representation = None
    dimension = 8

    def __init__(self) -> None:
        i=0
        while i <self.dimension:
            j=0
            while j <self.dimension:
                self.squares.append(Square(i,j))
                j += 1
            i+=1

    def get_square(self,coordinate):
        
        return next(square for square in self.squares if square.get_coordinates() == coordinate)  
    
    def _add_foot_coordinates(self):
        footer = "     a       b       c       d       e       f       g       h    "
        self._representation += footer
    
    def _print_pixels_of_square(self,file,column):
        square = next(square for square in self.squares if square.get_numeral_coordinates() == (column,file))
        self._representation += square.print()

    def _print_pixels_on_file(self,file):
        i = 0
        while i<self.dimension:
            self._print_pixels_of_square(file,i)
            i+=1
    
    def _return_horizontal_coordinate_or_spacer(self,iteration,line):
        if iteration == 0:
            return str(self.dimension-line) + " "
        return "  "
        
    
    def _print_line_of_pixels_on_file(self,file,times):
        i=0
        while i <times:
            self._representation += self._return_horizontal_coordinate_or_spacer(i,file)
            self._print_pixels_on_file(file)
            i+=1

    def _print_files(self):
        i = 0

        while i<self.dimension:
            self._print_line_of_pixels_on_file(i,4)
            i+=1

    def toString(self):
        self._representation = ""
        self._print_files()
        self._add_foot_coordinates()

        return self._representation

        
    