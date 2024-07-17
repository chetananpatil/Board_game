class Board:
    def __init__(self, squares):
        self.squares = squares
    
    def get_square(self, position):
        return self.squares[position]
