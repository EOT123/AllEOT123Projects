class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level
        health1  = the_level * 7

    def __repr__(self):
        return "{}, Level {}".format(
            self.name, self.level
        )
