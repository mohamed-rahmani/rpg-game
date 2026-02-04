import random


class Wizard:
    def __init__(self, degat, chance, fuite, prix, type_unite):
        self.degat = random.randint(2, 4)
        self.chance = 20
        self.prix = 15
        self.type_unite = "wizard"