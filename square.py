class Square():
    _file = 0
    _column = 0

    def __init__(self, column = 0, file = 0) -> None:
        self._file = file

    def get_coordinates(self):
        file_coordinate = self._file + 1
        
        return "a" + str(file_coordinate)
