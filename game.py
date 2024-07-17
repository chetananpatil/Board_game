from dice import Dice
from player.py import Player
from board import Board

class Game:
    def __init__(self, player1, player2, board):
        self.players = [player1, player2]
        self.board = board
        self.dice = Dice()
        self.current_player_index = 0
    
    def display_board(self):
        board_representation = ["_"] * len(self.board.squares)
        for player in self.players:
            board_representation[player.position] = player.name[0]
        print("Board: " + " ".join(board_representation))
    
    def check_win_condition(self):
        for player in self.players:
            if player.balance - player.debt > 100:
                print(f"{player.name} wins!")
                return True
            if player.debt - player.balance > 100:
                print(f"{player.name} loses!")
                return True
        return False
    
    def play_turn(self):
        player = self.players[self.current_player_index]
        
        if player.miss_next_turn:
            print(f"{player.name} misses this turn.")
            player.miss_next_turn = False
        else:
            steps = self.dice.roll()
            print(f"{player.name} rolls a {steps}.")
            player.move(steps, len(self.board.squares))
            self.process_square(player)
        
        if self.check_win_condition():
            return True
        
        self.current_player_index = (self.current_player_index + 1) % 2
        return False
    
    def process_square(self, player):
        square = self.board.get_square(player.position)
        if square == 'B':
            self.process_bank_square(player)
        elif square == 'J':
            self.process_jail_square(player)
        elif square == 'H':
            self.process_house_square(player)
    
    def process_bank_square(self, player):
        player.balance += 10
        print(f"{player.name} lands on a Bank. Balance increases by 10.")
        choice = input(f"{player.name}, do you want to take a loan? (yes/no): ").strip().lower()
        if choice == 'yes':
            loan_amount = min(10 * player.balance, 100)
            player.balance += loan_amount
            player.debt += loan_amount
            print(f"{player.name} takes a loan of {loan_amount}.")
        choice = input(f"{player.name}, do you want to repay your loan? (yes/no): ").strip().lower()
        if choice == 'yes':
            repay_amount = min(player.balance, player.debt)
            player.balance -= repay_amount
            player.debt -= repay_amount
            print(f"{player.name} repays {repay_amount} of the loan.")
    
    def process_jail_square(self, player):
        player.balance -= 20
        player.miss_next_turn = True
        print(f"{player.name} lands on Jail. Balance decreases by 20 and misses next turn.")
    
    def process_house_square(self, player):
        if player.balance > 0:
            player.balance += 2
        else:
            player.balance -= 2
        if player.debt > 0:
            player.debt += 1
        print(f"{player.name} lands on a House. Balance and Debt adjusted.")
        other_player = self.players[(self.current_player_index + 1) % 2]
        if other_player.position == player.position and player.balance > 0:
            transfer_amount = (player.balance + 1) // 2
            player.balance -= transfer_amount
            other_player.balance += transfer_amount
            print(f"{other_player.name} receives {transfer_amount} from {player.name}.")
