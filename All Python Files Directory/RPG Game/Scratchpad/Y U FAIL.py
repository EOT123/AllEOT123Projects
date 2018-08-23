import random
#import pickle
import shelve
#import time
from Actors import Hero, Creature

legal_locs_x = 0, 1, 2, 3, 4, 5
legal_locs_y = 0, 1, 2, 3, 4, 5
potion = (random.randint(0, 100))
myxpos = 0
myypos = 0
expos = (random.randint(0, 5))
eypos = (random.randint(0, 5))
Xp = 0
Player_Lvl = 0
extra_health = int(Player_Lvl) * 5
health = 100 + int(extra_health)
healthe = 10
Currency = 0
kill = 0
boss_kill = 0
current_room = (myxpos, myypos)


def main():
    print_header()
    game_loop()


def print_header():
    print('_________________________________')
    print("Welcome To This Game")
    print("Enter P For Controls")
    print("Enter N To Exit")
    print("Actions Are Not Case Sensitive")
    print("To Save Choose Save1, Save2, Or Save3")
    print('_________________________________')
    print()


def controls():
    print("P= Controls")
    print("Not Case Sensitive")
    print("To Save Choose Save1, Save2, Or Save3")
    print("E= Use Potion")
    print("A= Move West")
    print("D= Move East")
    print("W= Move North")
    print("S= Move South")
    print("Q= My Current Location/")
    print("You Can Combine Directions, Example: wd = Move Northeast")
    print("N= Exit Game")


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
        response = input("New game Or Load game? (Choose load1, load2, load3, Or new): ")
        print()
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

    while health >= 0:
        print()

        def battle_sequence():
            global healthe
            global action
            Random_Creature = random.choice(creatures)
            print("You Are Fighting A {}".format(Random_Creature))
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
        print()
        if (expos, eypos) == (myxpos, myypos):
            print("Enemy Is Here")
            battle_sequence()
            expos = (random.randint(0, 5))
            eypos = (random.randint(0, 5))
            print("Enemy {}, {}".format(expos, eypos))

        action = input('What Is Your Move? : ')

        if action == "p" or action == "P":
            controls()

        if potion == 0:
            potion = potion + 1
            print("You Are Out Of Potions")
        elif action == "e" or action == "E":
            potion = potion - 1
            print("You Have {} Potions Remaining".format(potion))
        elif action == "a" or action == "A":
            myxpos = myxpos - 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "d" or action == "D":
            myxpos = myxpos + 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "s" or action == "S":
            myypos = myypos - 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "w" or action == "W":
            myypos = myypos + 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "q" or action == "Q":
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "wa" or action == "WA":
            myxpos = myxpos - 1
            myypos = myypos + 1
            print("You Are Standing At {},{}".format(myxpos, myypos))
        elif action == "wd" or action == "WD":
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
            print("You Are Now Exiting This Game")
            break

        elif action == "v":
            Xp = Xp + 10000
            print("My Xp {}".format(Xp))

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


'''
Failed Ideas...Yay:
Possibly For Rooms?
    #legal_locs = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    #              (2, 0),
    #              (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 0),
    #              (4, 1),
    #              (4, 2), (4, 3), (4, 4), (4, 5), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]

        elif myxpos >= legal_locs:
            myxpos = myxpos - 1
        elif myxpos <= legal_locs:
            myxpos = myxpos + 1
        elif myypos >= legal_locs:
            myypos = myypos - 1
        elif myypos <= legal_locs:
            myypos = myypos + 1

        elif myxpos >= legal_locs_x:
            myxpos = myxpos - 1
        elif myxpos <= legal_locs_x:
            myxpos = myxpos + 1
        elif myypos >= legal_locs_y:
            myypos = myypos - 1
        elif myypos <= legal_locs_y:
            myypos = myypos + 1
________________________________________________________________________________________________________________________
Possible New Additions:
Bosses?/Xp For Bosses/Loot For Bosses
Nothing Else To See Here
________________________________________________________________________________________________________________________
TODO:
Enemies + Plus Naming Such Enemies []
Rooms aka 5x5 area for now []
Currency System And Shop []
Random Loot For Enemies []
Progressing Better Loot For Higher Enemies []
Perk System For Certain Classes []
Health System []
Picking Up Loot And Inventory []
________________________________________________________________________________________________________________________
Complete:
Saving System(For Now) [x]
Movement Between Coordinates [x]
Potion Drinking System [x]
Controls(For Now) [x]
Battle System [x]
Random Enemy Spawns [x]
Random Enemies In Random Enemy Spawns [x]
XP And Leveling System [x]
________________________________________________________________________________________________________________________
Future Possibly:
A Visual Version Of The Game
A TTS Version Of This Game
A 3 Dimensional Version Of This Game In OpenGL Or A 3D Engine
Figuring Out The Process Of Porting A Game Onto Consoles?
Maybe Breaking My Habit Of Liking Every Word To Begin With A Capital Letter? Nah
Random Place Holder Idea
________________________________________________________________________________________________________________________
        '''


if __name__ == '__main__':
    main()
