class Square():
    _file = ""
    _column = ""

    def __init__(self, column = 0, file = 0) -> None:
        self._file = file

    def get_coordinates(self):
        if self._file == 0:
            return "a1"
        
        return "a2"
