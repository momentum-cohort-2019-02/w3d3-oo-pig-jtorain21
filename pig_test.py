import random


class Dice:
    """Simulates a roll, by giving each player a value from 1-6
    """
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.choice(range(1, 6))

class Player:
    """
    """

