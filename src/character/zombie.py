import random


class Zombie:
    def __init__(self):
        self.degat = random.randint(1, 2)
        self.loot = random.randint(5, 10) / 10 
