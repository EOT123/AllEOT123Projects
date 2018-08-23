import random
healthe = 10
health = 10


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "{}, Level {}".format(
            self.name, self.level
        )

def game_loop():

    creatures = [
        Creature('Random PlaceHolder Name', 1),
        Creature('c2', 1),
        Creature('c3', 1),
        Creature('c4', 1),
        Creature('c5', 1),
        Creature('c6', 1),
    ]

    while health >= 0:
        print()

        def battle_sequence():
            global healthe
            global action
            Random_Creature = random.choice(creatures)
            print("You Are Fighting {}".format(Random_Creature))
            print("Battle Has Started")
            while healthe >= 0:
                action = input('What Is Your Move? : ')
                print()
                if action == "a":
                    healthe = healthe - 1
                    print("Enemy Health Is {}".format(healthe))
                if healthe == 0:
                    healthe = 10
                    print("You Have Won!")
                    print()
                    break
        action = input(": ")
        if action == "p":
            battle_sequence()


game_loop()
