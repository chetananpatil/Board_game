class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 5
        self.debt = 0
        self.position = 0
        self.miss_next_turn = False
    
    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size
    
    def display_status(self):
        print(f"{self.name}'s Balance: {self.balance}, Debt: {self.debt}")
