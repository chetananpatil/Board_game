from game import Game
from player import Player
from board import Board

def main():
    player1 = Player("Player1")
    player2 = Player("Player2")
    board = Board("HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH")
    game = Game(player1, player2, board)
    
    while True:
        game.display_board()
        for player in game.players:
            player.display_status()
        if game.play_turn():
            break

if __name__ == "__main__":
    main()
