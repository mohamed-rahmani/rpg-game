import random


class Hunter:
    def __init__(self):
        self.degat = random.choice(range(1, 3))
        self.chance = 10
        self.fuite = 20
        self.prix = 25
        self.type_unite = "hunter"

    def __repr__(self):
        return (
            f"Hunter(degat={self.degat}, chance={self.chance}, "
            f"fuite={self.fuite}, prix={self.prix}, "
            f"type_unite='{self.type_unite}')"
        )
