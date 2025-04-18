class Converter():
    
    def get_coordinates(self,file,column):
        file_coordinate = file + 1
        column_coordinate = column + ord("a")
        
        return chr(column_coordinate) + str(file_coordinate)