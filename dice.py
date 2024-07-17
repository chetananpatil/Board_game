import random

class Dice:
    def roll(self):
        roll = random.choices([1, 2, 3, 'RollAgain'], weights=[0.4, 0.2, 0.2, 0.2])[0]
        if roll == 'RollAgain':
            return self.roll()
        return roll
