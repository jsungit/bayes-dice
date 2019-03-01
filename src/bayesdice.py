import random
import scipy as scs


class BayesDice:
    def __init__(self):
        self.dice = [4, 6, 8, 12, 20]
        self.data = {die: 0.20 for die in self.dice}

    def choose_die(self):
        self.die = random.choice(self.dice)

    def roll_die(self):
        return random.randint(1, self.die)

    def update_priors(self, roll):
        print('before update:', self.data)
        denominator = list(map(lambda die: (0 if roll > die else (1 / die)) * self.data[die], self.dice))
        self.data = {self.dice[i]: numerator / sum(denominator) for i, numerator in enumerate(denominator)}
        self.debug(roll, denominator)

    def debug(self, roll, denominator):
        print('die:', self.die, 'roll:', roll)
        print('denominator:', denominator)
        print('data:', self.data)
        print('sum of priors:', sum(self.data.values()))
        print('sum of denominator:', sum(denominator))
        print('-' * 50)
