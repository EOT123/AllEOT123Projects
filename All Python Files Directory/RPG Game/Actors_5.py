class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.weapon = ''
        self.hp = 0
        self.mp = 0
        self.level = 1
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level
        health1 = the_level * 7

    def __repr__(self):
        return "{}, Level {}".format(
            self.name, self.level
        )
