## Assumptions

- Players input valid choices when prompted (yes/no).
- The board configuration is predefined and does not change.
- The game ends as soon as a winning condition is met.

## Classes and Files

- `dice.py`: Contains the `Dice` class to simulate the loaded dice.
- `player.py`: Contains the `Player` class to represent a player.
- `board.py`: Contains the `Board` class to represent the game board.
- `game.py`: Contains the `Game` class to manage game logic and state.
- `main.py`: The main entry point to start the game.

## Example Board

The board is initialized with the following squares:
HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH

Where:
- `H` is a House square.
- `B` is a Bank square.
- `J` is a Jail square.


## Gameplay

1. Players start at the initial position with a balance of 5 and debt of 0.
2. Players take turns to roll the dice and move their pieces around the board.
3. Players interact with different squares based on the rules defined in the game.
4. The game ends when one player wins or loses based on their net balance or debt.

## Game Rules

- **Bank Square**: Player gains 10 balance, can take a loan, and can repay a loan.
- **Jail Square**: Player loses 20 balance and misses the next turn.
- **House Square**: Adjusts balance and debt based on current balance and debt.
- **Loaded Dice**: Dice with probabilities for 1, 2, 3, and "Roll Again".
