
class InvalidSquareException(Exception):
    pass
class Square():
    _file = 0
    _column = 0

    def __init__(self, column = 0, file = 0) -> None:

        if column > 7 or file > 7:
            raise InvalidSquareException("Invalid Square Coordinate")

        self._file = file
        self._column = column

    def get_coordinates(self):
        file_coordinate = self._file + 1
        column_coordinate = self._column + ord("a")
        
        return chr(column_coordinate) + str(file_coordinate)
    
    def isBlack(self):
        if self._file % 2 == 0:
            return self._column % 2 == 0
        
        return self._column % 2 == 1
