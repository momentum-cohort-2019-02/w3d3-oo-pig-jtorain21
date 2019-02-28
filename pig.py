import random


class Die:
    """Simulates a roll, by giving each player a value from 1-6
    """
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.choice(range(1, 6))


class Game:
    def __init__(self, first_turn, player, computer, roll):
        self.first_turn = random.randint(1, 2)
        self.player = player
        self.computer = computer
        self.roll = self.die.roll
        self.counter = 0

    def choose_player(self):
        if self.first_turn == 1:
            return "You go first"
        else:
            return "Computer goes first"

    
class Player:
    """Keeps track of player's turn score, and overall game score
    """
    def __init__(self, turn_score, overall_score):
        self.turn_score = turn_score
        self.overall_score = overall_score


class Computer:
    """Keeps track of Computers turn score, and overall game score.  Also makes sure that the computer always holds after it reaches 20 points.
    """
    def __init__(self, turn_score, overall_score):
        self.overall_score = 0

    def computer_score(self, computer):
        computer.turn_score = 0
        while computer.turn_score < 20:
            roll = Die.roll()
            if roll == 1:
                return 0
        else:
            return roll
