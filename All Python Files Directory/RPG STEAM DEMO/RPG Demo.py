"""--------------------This Is A Demo For STEAM Fair----------------Game Is A WIP----------------------------------- """

# Import Functions------------------------------------------------------------------------------------------------------
import random
import shelve
from Actors import Hero, Creature

# Variables-------------------------------------------------------------------------------------------------------------
potion = (random.randint(0, 100))  # Potions WIP
myxpos = 0  # Player Position X-Axis
myypos = 0  # Player Position Y-Axis
expos = (random.randint(0, 5))  # Enemy Position X-Axis
eypos = (random.randint(0, 5))  # Enemy Position Y-Axis
Xp = 0  # Player XP WIP
Player_Lvl = 0  # Player Level
extra_health = int(Player_Lvl) * 5  # Health Multiplier Per Level WIP
health = 100 + int(extra_health)  # Player Total Health WIP
healthe = 10  # Enemy Health
Currency = 0  # Money WIP
kill = 0  # Kill Count WIP
boss_kill = 0  # Boss Kill Count WIP
current_room = (myxpos, myypos)  # Current Location
inventory = []  # Inventory WIP


def main():
    controls()
    print_header()
    game_loop()


def print_header():
    print("Version: Development")
    print('___________________________________________________________________________________________________________')
    print("Welcome To This Game")
    print("Enter P For Controls")
    print("Enter N To Exit")
    print("Actions Are Not Case Sensitive")
    print("To Save Choose Save1, Save2, Or Save3")
    print('___________________________________________________________________________________________________________')
    print()


def controls():
    print("P = Controls")
    print("Not Case Sensitive")
    print("To Save Choose Save1, Save2, Or Save3")
    print("E = Use Potion")
    print("A or West = Move West")
    print("D or East = Move East")
    print("W or North = Move North")
    print("S or South = Move South")
    print("Q = My Current Location/")
    print("You Can Combine Directions, Example: wd = Move Northeast")
    print("N = Exit Game")


def game_loop():
    global healthe
    global action
    global expos
    global eypos
    global myxpos
    global myypos
    global potion
    global Xp
    creatures = [
        Creature('Random PlaceHolder Name', 1),
        Creature('c2', 1),
        Creature('c3', 1),
        Creature('c4', 1),
        Creature('c5', 1),
        Creature('c6', 1),
    ]

    hero = Hero('Generic Name', 1)

    response = input("Start A New Game Or Load A Game? (Enter load1, load2, load3, Or New): ")
    while response != "load1" and response != "Load1" and response != "LOAD1" and response != "load2" \
            and response != "Load2" and response != "LOAD2" and response != "load3" and response != "Load3" \
            and response != "LOAD3" and response != "new":
        print(response + " is invalid input")
        response = input("New game Or Load game? (Choose new, or load1, load2, load3): ")
        print()
# Saves-----------------------------------------------------------------------------------------------------------------
    if response == "load1":
        try:
            f = shelve.open("save1.dat")
            attributes = f["attributes"]
            f.close()
            Name = attributes["Name"]
            Race = attributes["Race"]
            Class = attributes["Class"]
            Weapon = attributes["Weapon"]
            Xp = attributes["Xp"]
            Player_Lvl = attributes["Player_Lvl"]
            Currency = attributes["Currency"]
            potion = attributes["potion"]
            myxpos = attributes["myxpos"]
            myypos = attributes["myypos"]
            print("You Are A {} Wielding A {}. Your Name Is {}.".format(Class, Weapon, Name))
            print(attributes)
        except:
            print("Save file is corrupt or doesn't exist")
            response = input("New game Or Load game? (Choose load1, load2, load3, Or new): ")
    elif response == "load2":
        try:
            f = shelve.open("save2.dat")
            attributes = f["attributes"]
            f.close()
            Name = attributes["Name"]
            Race = attributes["Race"]
            Class = attributes["Class"]
            Weapon = attributes["Weapon"]
            Xp = attributes["Xp"]
            Player_Lvl = attributes["Player_Lvl"]
            Currency = attributes["Currency"]
            potion = attributes["potion"]
            myxpos = attributes["myxpos"]
            myypos = attributes["myypos"]
            print("You Are A {} Wielding A {}. Your Name Is {}.".format(Class, Weapon, Name))
            print(attributes)
        except:
            print("Save file is corrupt or doesn't exist")
            response = "not"
    elif response == "load3":
        try:
            f = shelve.open("save3.dat")
            attributes = f["attributes"]
            f.close()
            Name = attributes["Name"]
            Race = attributes["Race"]
            Class = attributes["Class"]
            Weapon = attributes["Weapon"]
            Xp = attributes["Xp"]
            Player_Lvl = attributes["Player_Lvl"]
            Currency = attributes["Currency"]
            potion = attributes["potion"]
            myxpos = attributes["myxpos"]
            myypos = attributes["myypos"]
            print("You Are A {} Wielding A {}. Your Name Is {}.".format(Class, Weapon, Name))
            print(attributes)
        except:
            print("Save file is corrupt or doesn't exist")
            response = "new"
    if response == "new":
        Name = input("What is your name?")
        Race = input("What is your race? (Your choices are Human, Cyborg, and Robot.): ")
        Class = input("What is your class? (Your choices are Assault, Sniper, and Mage.: ")
        if Race == "Robot" or Race == "robot" or Race == "ROBOT":
            Race = "Robot"
        elif Race == "Human" or Race == "human" or Race == "HUMAN":
            Race = "Human"
        elif Race == "Cyborg" or Race == "cyborg" or Race == "CYBORG":
            Race = "Cyborg"

        if Class == "Assault" or Class == "assault":
            Weapon = "Electric Rifle"
            Class = "Assault"
            print("You Are A {} Wielding A {}. Your Name Is {}.".format(Class, Weapon, Name))
        elif Class == "Sniper" or Class == "sniper":
            Weapon = "Pulse Sniper"
            Class = "Sniper"
            print("You Are A {} Wielding A {}. Your Name Is {}.".format(Class, Weapon, Name))
        elif Class == "Mage" or Class == "mage":
            Weapon = "Staff"
            Class = "Mage"
            print("You Are A {} Wielding A {}. Your Name Is {}.".format(Class, Weapon, Name))
        else:
            print("Not A Valid Choice")

    print("You Are Starting At ({}, {})".format(myxpos, myypos))
    print("You Are Starting With {} Potions".format(potion))
    print("Enemy {}, {}".format(expos, eypos))
    print()
    while True:
        print()

# A Area Of The Code That Starts A Battle Phase-------------------------------------------------------------------------
        def battle_sequence():
            global healthe
            global action
            Random_Creature = random.choice(creatures)
            print("You Are Fighting A {}".format(Random_Creature))
            print("Battle Has Started")
            print("Enter 'A' To Attack")
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
# Enemy Spawn-----------------------------------------------------------------------------------------------------------
        print()
        if (expos, eypos) == (myxpos, myypos):
            print("Enemy Is Here")
            battle_sequence()
            expos = (random.randint(1, 5))
            eypos = (random.randint(1, 5))
            print("Enemy {}, {}".format(expos, eypos))
# Controls--------------------------------------------------------------------------------------------------------------
        action = input('What Is Your Move? : ')
        print("Enemy Position Is {}, {}".format(expos, eypos))

        if action == "p" or action == "P":
            controls()

        if potion == 0:
            potion = potion + 1
            print("You Are Out Of Potions")
        elif action == "e" or action == "E":
            potion = potion - 1
            print("You Have {} Potions Remaining".format(potion))
        elif action == "West" or action == "WEST" or action == "west" or action == "a" or action == "A":
            myxpos = myxpos - 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "East" or action == "EAST" or action == "east" or action == "d" or action == "D":
            myxpos = myxpos + 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "South" or action == "SOUTH" or action == "south" or action == "s" or action == "S":
            myypos = myypos - 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "North" or action == "NORTH" or action == "north" or action == "w" or action == "W":
            myypos = myypos + 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "q" or action == "Q":
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "Northwest" or action == "NORTHWEST" or action == "northwest" or action == "wa" or action == "WA":
            myxpos = myxpos - 1
            myypos = myypos + 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "NORTHEAST" or action == "Northeast" or action == "northeast" or action == "wd" or action == "WD":
            myxpos = myxpos + 1
            myypos = myypos + 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "sa" or action == "SA":
            myxpos = myxpos - 1
            myypos = myypos - 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "sd" or action == "SD":
            myxpos = myxpos + 1
            myypos = myypos - 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "n" or action == "N":
            if input("Are You Sure? (Y/N): ") == "y":
                print("You Are Now Exiting This Game")
                break
            elif action == "N" or action == "n":
                print("Continuing")
                pass

        elif action == "v":
            Xp = Xp + 10000
            print("My Xp {}".format(Xp))
# Saves-----------------------------------------------------------------------------------------------------------------
        elif action == "save1" or action == "SAVE1" or action == "Save1":
            f = shelve.open("save1.dat")
            attributes = {"Name": Name, "Race": Race, "Class": Class, "Weapon": Weapon, "Xp": Xp,
                          "Player_Lvl": Player_Lvl, "Currency": Currency, "potion": potion, "myxpos": myxpos,
                          "myypos": myypos}
            f["attributes"] = attributes
            f.sync()
            f.close()
            print("Game saved")
            break
        elif action == "save2" or action == "SAVE2" or action == "Save2":
            f = shelve.open("save2.dat")
            attributes = {"Name": Name, "Race": Race, "Class": Class, "Weapon": Weapon, "Xp": Xp,
                          "Player_Lvl": Player_Lvl, "Currency": Currency, "potion": potion, "myxpos": myxpos,
                          "myypos": myypos}
            f["attributes"] = attributes
            f.sync()
            f.close()
            print("Game saved")
            break
        elif action == "save3" or action == "SAVE3" or action == "Save3":
            f = shelve.open("save3.dat")
            attributes = {"Name": Name, "Race": Race, "Class": Class, "Weapon": Weapon, "Xp": Xp,
                          "Player_Lvl": Player_Lvl, "Currency": Currency, "potion": potion, "myxpos": myxpos,
                          "myypos": myypos}
            f["attributes"] = attributes
            f.sync()
            f.close()
            print("Game saved")
            break
# Levels----------------------------------------------------------------------------------------------------------------
        if 0 <= Xp <= 9:
            Player_Lvl = 0
        elif 10 <= Xp <= 39:
            Player_Lvl = 1
        elif 40 <= Xp <= 79:
            Player_Lvl = 2
        elif 80 <= Xp <= 159:
            Player_Lvl = 3
        elif 160 <= Xp <= 319:
            Player_Lvl = 4
        elif 320 <= Xp <= 639:
            Player_Lvl = 5
        elif 640 <= Xp <= 1279:
            Player_Lvl = 6
        elif 1280 <= Xp <= 2559:
            Player_Lvl = 7
        elif 2560 <= Xp <= 5119:
            Player_Lvl = 8
        elif 5120 <= Xp <= 10239:
            Player_Lvl = 9
        elif 10240 <= Xp <= 20479:
            Player_Lvl = 10
        elif 20480 <= Xp <= 40959:
            Player_Lvl = 11
        elif 40960 <= Xp <= 81919:
            Player_Lvl = 12
        elif 81920 <= Xp <= 163839:
            Player_Lvl = 13
        elif 163840 <= Xp <= 327679:
            Player_Lvl = 14
        elif 327680 <= Xp <= 655359:
            Player_Lvl = 15
        elif 655360 <= Xp <= 1310719:
            Player_Lvl = 16
        elif 1310720 <= Xp <= 2621439:
            Player_Lvl = 17
        elif 2621440 <= Xp <= 5242879:
            Player_Lvl = 18
        elif 5242880 <= Xp <= 10485759:
            Player_Lvl = 19
        elif 10485760 <= Xp <= 20971519:
            Player_Lvl = 20
        elif 20971520 <= Xp <= 41943039:
            Player_Lvl = 21
        elif 41943040 <= Xp <= 83886079:
            Player_Lvl = 22
        elif 83886080 <= Xp <= 167772159:
            Player_Lvl = 23
        elif 167772160 <= Xp <= 335544319:
            Player_Lvl = 24
        elif 335544320 <= Xp <= 671088640:
            Player_Lvl = 25
        else:
            print("This Is Not A Valid Action, Check If You Made A Typo")


if __name__ == '__main__':
    main()


