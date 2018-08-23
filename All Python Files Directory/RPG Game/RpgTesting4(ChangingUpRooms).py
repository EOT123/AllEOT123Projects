"""
Game Version Info:
[Major build number].[Minor build number].[Revision].[Package]

i.e. Version: 1.0.15.2

Major build number: This indicates a major milestone in the game, increment this when going from beta to release, from
 release to major updates.

Minor build number: Used for feature updates, large bug fixes etc.

Revision: Minor alterations on existing features, small bug fixes, etc.

Package: Your code stays the same, external library changes or asset file update."""
import random
import sys
import os
# import pickle
import shelve
import time
from Actors_3 import player, Creature
import Rooms

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
                 'e1': False, 'e2': False, 'e3': False, 'e4': False, 'e5': False,
                 }


rooms = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'a5',
    },
    'a5': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b5',
        LEFT: 'a4',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "Home",
        DESCRIPTION: 'This Is Your Home',
        EXAMINATION: 'Your Home Looks The Same - Nothing Has Changed',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'b5',
    },
    'b5': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a5',
        DOWN: 'c5',
        LEFT: 'b4',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'c5',
    },
    'c5': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b5',
        DOWN: 'd5',
        LEFT: 'c4',
        RIGHT: '',
    },
    'd1': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'e1',
        LEFT: '',
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c2',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'e3',
        LEFT: 'd2',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c4',
        DOWN: 'e4',
        LEFT: 'd3',
        RIGHT: 'd5',
    },
    'd5': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'c5',
        DOWN: 'e5',
        LEFT: 'd4',
        RIGHT: '',
    },
    'e1': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },
    'e2': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },
    'e3': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },
    'e4': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },
    'e5': {
        ZONENAME: " ",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },
}

potion = (random.randint(0, 100))
mypos = 1
# epos = random.choice(rooms)
# extra_health = int(Player_Lvl) * 5
# health = 100 + int(extra_health)
healthe = 10
Currency = 0
kill = 0
boss_kill = 0
current_room = mypos
myPlayer = player()
# myPlayer.level = Player_Lvl
inventory = []


def title_screen_selection():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        quit_game_1()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please Enter A Valid Command")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            quit_game_1()


def title_screen():
    print('__________________________________')
    print('_ Welcome To The Random Text RPG _')
    print('__________________________________')
    print('             _ Play _             ')
    print('             _ Help _             ')
    print('             _ Quit _             ')
    title_screen_selection()


def help_menu():
    print('__________________________________')
    print('_ Welcome To The Random Text RPG _')
    print('__________________________________')
    print('- Use Up, Down, Left, Right To Move -')
    print('- Type Your Commands To Do Them -')
    print('- Use "Look" To Inspect Something -')
    print('- Good Luck And Have Fun! -')
    print('- Continue For All Commands')
    help_action = input('Continue? Y/N \n' + '> ')
    acceptable_help = ['y', 'n', 'yes', 'no', 'continue']
    while help_action.lower() not in acceptable_help:
        print("Unknown Action, Try Again.\n")
        help_action = input('Continue? Y/N \n' + '> ')
    if help_action.lower() in ['y', 'yes', 'continue']:
        controls_1()
    elif help_action.lower() in ['n', 'no']:
        title_screen()


def print_location():
    print('\n' + '_' * (4 + len(rooms[myPlayer.location][DESCRIPTION])))
    print('| ' + rooms[myPlayer.location][ZONENAME].upper() + ' ' * (len(rooms[myPlayer.location][DESCRIPTION])) + '|')
    print('| ' + rooms[myPlayer.location][DESCRIPTION] + ' |')
    print('_' * (4 + len(rooms[myPlayer.location][DESCRIPTION])))


Xp = 0
Player_Lvl = 0
Xp_Next_Lvl = 40


def xp_gain():
    global Xp
    global Player_Lvl
    global Xp_Next_Lvl
    while Xp >= Xp_Next_Lvl:
        Player_Lvl += 1
        Xp = Xp - Xp_Next_Lvl
        Xp_Next_Lvl = round(Xp_Next_Lvl * 1.2)

    print("Level Is {}".format(Player_Lvl))
    print("Xp Is {}".format(Xp))
    print("{}% To Next Level".format(int((Xp / Xp_Next_Lvl)*100)))
    print("Xp To Next Level Is {}".format(Xp_Next_Lvl))


def xp_cheat():
    global Xp
    Xp += 10
    print("Level Is {}".format(Player_Lvl))
    print("Xp Is {}".format(Xp))
    print("{}% To Next Level".format(int((Xp / Xp_Next_Lvl)*100)))
    print("Xp To Next Level Is {}".format(Xp_Next_Lvl))


def prompt():
    global Xp
    print("\n" + "__________________________")
    print("What Would You Like To Do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'level',
                          'help', 'control', 'controls', 'test', 'location', 'position', 'die', 'xp', 'xp_up']
    while action.lower() not in acceptable_actions:
        print("Unknown Action, Try Again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        quit_game_2()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
    elif action.lower() in ['help', 'control', 'controls', 'commands']:
        controls_2()
    elif action.lower() in ['test']:
        player_test()
    elif action.lower() in ['location', 'position']:
        print_location()
    elif action.lower() in ['die']:
        die()
    elif action.lower() in ['xp', 'level']:
        xp_gain()
    elif action.lower() in ['xp_up']:
        xp_cheat()


def player_move(myAction):
    ask = "Where Would You Like To Move To?\n> "
    dest = input(ask)
    if dest in ['up', 'north', 'u', 'n']:
        destination = rooms[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south', 'd', 's']:
        destination = rooms[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west', 'l', 'w']:
        destination = rooms[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east', 'r', 'e']:
        destination = rooms[myPlayer.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You Have Moved To The " + destination.title() + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if rooms[myPlayer.location][SOLVED]:
        print("You Have Already Exhausted This Zone.")
    else:
        print("You Can Trigger A Puzzle Here.")


def player_test():
    ask = "What Do You Want To Test?\n> "
    test = input(ask)
    if test in ['name']:
        print("Name Is " + myPlayer.name)
    elif test in ['class', 'job', 'role']:
        print("Class Is " + myPlayer.job.title())
    elif test in ['weapon']:
        print("Weapon Is " + myPlayer.weapon.title())
    elif test in ['stats', 'stat']:
        print("Stats Are ")


def quit_game_1():
    ask = "Are You Sure You Want To Quit?\n> "
    quitting = input(ask)
    if quitting in ['yes', 'continue', 'y']:
        quit()
    elif quitting in ['no', 'n']:
        title_screen()


def quit_game_2():
    ask = "Are You Sure You Want To Quit?\n> "
    quitting = input(ask)
    if quitting in ['yes', 'continue', 'y']:
        quit()
    elif quitting in ['no', 'n']:
        main_game_loop()


def restart():
    ask = "______________________________\nDo You Want To Restart?\n> "
    restarting = input(ask)
    if restarting in ['yes', 'continue', 'y']:
        title_screen()
    elif restarting in ['no', 'n']:
        print("______________________________\nClosing Game")
        quit()


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()


def print_header():
    print("Version: Development")
    print('_________________________________')
    print("Welcome To This Game")
    print("Type 'Help' For Commands")
    print("Type 'Quit' To Exit")
    print("Commands Are Not Case Sensitive")
    print("To Save Choose Save1, Save2, Or Save3")
    print('_________________________________')
    print()


def controls_print():
    print("________________________________________\nAll Commands\n________________________________________")
    print("Use = Use an Item")
    print("________________________________________\n1)Movement:\nGo, Move, Travel, Walk\n2)Directions:\n"
          "(North, Up, N, U)\n(West, Left, W, L)\n(East, Right, E, R)\n(South, Down, S, D)")
    print("________________________________________\nExamine, Look, Inspect Interact () = Look At A Object")
    print("________________________________________")
    print("Quit, Leave, Exit, Close = Exit The Game")


def controls_1():
    controls_print()
    controls_1_action = input('Continue?\n' + '> ')
    acceptable_controls_1 = ['y', 'yes', 'continue']
    while controls_1_action.lower() not in acceptable_controls_1:
        print("Unknown Action, Try Again.\n")
        controls_1_action = input('Continue?\n' + '> ')
    if controls_1_action.lower() in ['y', 'yes', 'continue']:
        title_screen()


def controls_2():
    controls_print()
    controls_2_action = input('Continue?\n' + '> ')
    acceptable_controls_2 = ['y', 'yes', 'continue']
    while controls_2_action.lower() not in acceptable_controls_2:
        print("Unknown Action, Try Again.\n")
        controls_2_action = input('Continue?\n' + '> ')
    if controls_2_action.lower() in ['y', 'yes', 'continue']:
        main_game_loop()


def die():
    die_action = input('How Do You Want To Die?\n> ')
    acceptable_die = ['inside', 'fall', 'jump', 'disaster', 'stab', 'shoot', 'dehydrate', 'starve', 'hang',
                      'hang myself', 'shoot myself', 'starve myself']
    while die_action.lower() not in acceptable_die:
        print('Not A Way To Die Here...Sorry ¯\_(ツ)_/¯')
        die_action = input('How Do You Want To Die?\n> ')
    if die_action.lower() in ['hang', 'hang myself']:
        dead_hang_list = ["hang"]
        dead_hang = random.choice(dead_hang_list)
        print(dead_hang)
        restart()
# check inventory for rope
    elif die_action.lower() in ['shoot', 'shoot myself']:
        dead_shoot_list = ["shoot"]
        dead_shoot = random.choice(dead_shoot_list)
        print(dead_shoot)
        restart()
# check inventory fo gun
    elif die_action.lower() in ['starve', 'starve myself']:
        dead_starve_list = ["starve"]
        dead_starve = random.choice(dead_starve_list)
        print(dead_starve)
        restart()
    elif die_action.lower() in ['dehydrate']:
        dead_dehydrate_list = ["dehydrate"]
        dead_dehydrate = random.choice(dead_dehydrate_list)
        print(dead_dehydrate)
        restart()
    elif die_action.lower() in ['fall', 'jump']:
        dead_jump_list = ["fall"]
        dead_jump = random.choice(dead_jump_list)
        print(dead_jump)
# check area for place to jump
        restart()
    elif die_action.lower() in ['stab']:
        dead_stab_list = ["stab"]
        dead_stab = random.choice(dead_stab_list)
        print(dead_stab)
        restart()
# check inventory for knife/sword
    elif die_action.lower() in ['inside']:
        dead_inside_list = ['You Believe You Are Dead Because All The "Pain" You Have Suffered Through',
                            'You Gave Up The Will To Live']
        dead_inside = random.choice(dead_inside_list)
        print(dead_inside)
        restart()
# add random quotes


def position():
    print("___________________________")
    print("You are in the " + rooms[current_room]["name"])
    print("Inventory : " + str(inventory))
    if "item" in rooms[current_room]:
        print("You see a " + rooms[current_room]["item"])
    print("___________________________")


def game_loop():
    global healthe
    global epos
    global potion
    creatures = [
        Creature('Random PlaceHolder Name', 1),
        Creature('c2', 1),
        Creature('c3', 1),
        Creature('c4', 1),
        Creature('c5', 1),
        Creature('c6', 1),
    ]

    while True:
        global current_room
        print()
        position()

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
        if epos == mypos:
            print("Enemy Is Here")
            battle_sequence()
            epos = (random.choice(rooms))
            print("Enemy {}".format(epos))

        # if potion == 0:
        #     potion = potion + 1
        #     print("You Are Out Of Potions")
        # elif action == "e" or action == "E":
        #     potion = potion - 1
        #     print("You Have {} Potions Remaining".format(potion))


def setup_game():
    """Name Collecting"""
    question1 = "Hello What Is Your Name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    """Job Handling"""
    question2 = "What Is Your Class?\n"
    question2added = "(You Can Choose An Assault, Sniper, Mage, Or Heavy)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['assault', 'Assault', 'ASSAULT', 'sniper', 'SNIPER', 'Sniper', 'mage', 'Mage', 'MAGE', 'heavy',
                  'Heavy', 'HEAVY', 'test_to_long_to_type', 'Test_to_long_to_type', 'TEST_TO_LONG_TO_TYPE']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You Are Now A " + player_job.title() + ".\n")
    while player_job.lower() not in valid_jobs:
        print("Not A Valid Class, Try Again")
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You Are Now A " + player_job.title() + ".\n")

    """Player Stats"""
    if myPlayer.job is 'assault':
        self.hp = 150
        self.mp = 40
    elif myPlayer.job is 'sniper':
        self.hp = 75
        self.mp = 60
    elif myPlayer.job is 'mage':
        self.hp = 100
        self.mp = 120
    elif myPlayer.job is 'heavy':
        self.hp = 250
        self.mp = 20
    elif myPlayer.job is 'test_to_long_to_type':
        self.hp = 999
        self.mp = 999

    """Weapon"""
    question3 = "What Is Your Starting Weapon?\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    if player_job == 'assault' or 'Assault' or 'ASSAULT':
        question3assault = "(You Can Choose A Assault Rifle, Sword)\n"
        for character in question3assault:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        player_weapon = input("> ")
        valid_weapon_assault = ['assault rifle', 'rifle', 'sword']
        if player_weapon.lower() in ['assault rifle', 'rifle']:
            player_weapon = 'assault rifle'
            myPlayer.weapon = player_weapon
        elif player_weapon.lower() in ['sword']:
            player_weapon = 'sword'
            myPlayer.weapon = player_weapon
        print("You Are Wielding A " + player_weapon.title() + ".\n")
        while player_weapon.lower() not in valid_weapon_assault:
            print("Not A Valid Choice, Try Again")
            player_weapon = input("> ")
            if player_weapon.lower() in ['assault rifle', 'rifle']:
                player_weapon = 'assault rifle'
                myPlayer.weapon = player_weapon
            elif player_weapon.lower() in ['sword']:
                player_weapon = 'sword'
                myPlayer.weapon = player_weapon
            print("You Are Wielding A " + player_weapon.title() + ".\n")
    elif player_job == 'sniper' or 'Sniper' or 'SNIPER':
        question3sniper = "(You Can Choose A Standard Sniper, Pulse Sniper MKI)\n"
        for character in question3sniper:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        player_weapon = input("> ")
        valid_weapon_sniper = ['standard sniper', 'standard', 'pulse sniper mki', 'pulse', 'pulse sniper mk1',
                               'pulse sniper']
        if player_weapon.lower() in ['standard sniper', 'standard']:
            player_weapon = 'standard sniper'
            myPlayer.weapon = player_weapon
            print("You Are Wielding A " + player_weapon.title() + ".\n")
        elif player_weapon.lower() in ['pulse sniper mki', 'pulse', 'pulse sniper mk1', 'pulse sniper']:
            player_weapon = 'pulse sniper mki'
            myPlayer.weapon = player_weapon
            print("You Are Wielding A Pulse Sniper MKI" + ".\n")
        while player_weapon.lower() not in valid_weapon_sniper:
            print("Not A Valid Choice, Try Again")
            player_weapon = input("> ")
            if player_weapon.lower() in ['standard sniper', 'standard']:
                player_weapon = 'standard sniper'
                myPlayer.weapon = player_weapon
            elif player_weapon.lower() in ['pulse sniper mki', 'pulse', 'pulse sniper mk1', 'pulse sniper']:
                player_weapon = 'pulse sniper MKI'
                myPlayer.weapon = player_weapon
            print("You Are Wielding A " + player_weapon.title() + ".\n")
    elif player_job == 'mage' or 'Mage' or 'MAGE':
        question3mage = "(You Can Choose A Staff, Spellbook)\n"
        for character in question3mage:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        player_weapon = input("> ")
        valid_weapon_mage = ['staff', 'spellbook', 'book', 'spell']
        if player_weapon.lower() in ['staff']:
            player_weapon = 'staff'
            myPlayer.weapon = player_weapon
        elif player_weapon.lower() in ['spellbook', 'book', 'spell']:
            player_weapon = 'spellbook'
            myPlayer.weapon = player_weapon
        print("You Are Wielding A " + player_weapon.title() + ".\n")
        while player_weapon.lower() not in valid_weapon_mage:
            print("Not A Valid Choice, Try Again")
            player_weapon = input("> ")
            if player_weapon.lower() in ['staff']:
                player_weapon = 'staff'
                myPlayer.weapon = player_weapon
            elif player_weapon.lower() in ['spellbook', 'book', 'spell']:
                player_weapon = 'spellbook'
                myPlayer.weapon = player_weapon
            print("You Are Wielding A " + player_weapon.title() + ".\n")
    elif player_job == 'heavy' or 'Heavy' or 'HEAVY':
        question3heavy = "(You Can Choose A Minigun, LMG)\n"
        for character in question3heavy:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        player_weapon = input("> ")
        valid_weapon_heavy = ['minigun', 'lmg', 'light machine gun']
        if player_weapon.lower() in ['minigun']:
            player_weapon = 'minigun'
            myPlayer.weapon = player_weapon
        elif player_weapon.lower() in ['lmg', 'light machine gun']:
            player_weapon = 'light machine gun'
            myPlayer.weapon = player_weapon
        print("You Are Wielding A " + player_weapon.title() + ".\n")
        while player_weapon.lower() not in valid_weapon_heavy:
            print("Not A Valid Choice, Try Again")
            player_weapon = input("> ")
            if player_weapon.lower() in ['minigun']:
                player_weapon = 'minigun'
                myPlayer.weapon = player_weapon
            elif player_weapon.lower() in ['lmg', 'light machine gun']:
                player_weapon = 'light machine gun'
                myPlayer.weapon = player_weapon
            print("You Are Wielding A " + player_weapon.title() + ".\n")
    elif player_job == 'test_to_long_to_type' or 'Test_to_long_to_type' or 'TEST_TO_LONG_TO_TYPE':
        question3test_to_long_to_type = "(You Can Choose A Demolisher666, NoScoper420, OPNerfGun, BanHammer)\n"
        for character in question3test_to_long_to_type:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        player_weapon = input("> ")
        valid_weapon_test_to_long_to_type = ['demolisher666', 'noscoper420', 'opnerfgun', 'banhammer']
        if player_weapon.lower() in ['demolisher666']:
            player_weapon = 'demolisher666'
            myPlayer.weapon = player_weapon
        elif player_weapon.lower() in ['noscoper420']:
            player_weapon = 'noscoper420'
            myPlayer.weapon = player_weapon
        elif player_weapon.lower() in ['opnerfgun']:
            player_weapon = 'opnerfgun'
            myPlayer.weapon = player_weapon
        elif player_weapon.lower() in ['banhammer']:
            player_weapon = 'banhammer'
            myPlayer.weapon = player_weapon
        print("You Are Wielding A " + player_weapon.title() + ".\n")
        while player_weapon.lower() not in valid_weapon_test_to_long_to_type:
            print("Not A Valid Choice, Try Again")
            player_weapon = input("> ")
            if player_weapon.lower() in ['demolisher666']:
                player_weapon = 'demolisher666'
                myPlayer.weapon = player_weapon
            elif player_weapon.lower() in ['noscoper420']:
                player_weapon = 'noscoper420'
                myPlayer.weapon = player_weapon
            elif player_weapon.lower() in ['opnerfgun']:
                player_weapon = 'opnerfgun'
                myPlayer.weapon = player_weapon
            elif player_weapon.lower() in ['banhammer']:
                player_weapon = 'banhammer'
                myPlayer.weapon = player_weapon
            print("You Are Wielding A " + player_weapon.title() + ".\n")
    """Introduction"""
    question4 = "Welcome, " + player_name + " The " + player_weapon.title() + " Wielding " + player_job.title() + ".\n"
    for character in question4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "Welcome To 'Place Holder Name'!\n"
    speech2 = "Or At This Point Of Time 'Very Bootleg Skyrim'...\n"
    speech3 = "Not My Choice To Make...\n"
    speech4 = "Call It Whatever You Want It Is Not Done Yet...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)

    print("_____________________")
    print("_ Game Starting Now _")
    print("_____________________")
    main_game_loop()


'''
________________________________________________________________________________________________________________________
Possible New Additions:
Bosses?/Xp For Bosses/Loot For Bosses
Nothing Else To See Here
________________________________________________________________________________________________________________________
TODO:
Fix Typing Assault, Sniper, Mage, Or Heavy Uppercase []
Enemies, Plus Naming Such Enemies [WIP]
Rooms aka 5x5 area for now [WIP]
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
Random Place Holder Idea
________________________________________________________________________________________________________________________
Old System
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
            mypos = attributes["mypos"]
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
            mypos = attributes["mypos"]
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
            mypos = attributes["mypos"]
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

    print("You Are Starting At ({})".format(mypos))
    print("You Are Starting With {} Potions".format(potion))
    print("Enemy {}".format(epos))
    print()
________________________________________________________________________________________________________________________
To Be Fixed:
        elif action == "save1" or action == "SAVE1" or action == "Save1":
            f = shelve.open("save1.dat")
            attributes = {"Name": Name, "Race": Race, "Class": Class, "Weapon": Weapon, "Xp": Xp,
                          "Player_Lvl": Player_Lvl, "Currency": Currency, "potion": potion, "mypos": mypos}
            f["attributes"] = attributes
            f.sync()
            f.close()
            print("Game saved")
            break
        elif action == "save2" or action == "SAVE2" or action == "Save2":
            f = shelve.open("save2.dat")
            attributes = {"Name": Name, "Race": Race, "Class": Class, "Weapon": Weapon, "Xp": Xp,
                          "Player_Lvl": Player_Lvl, "Currency": Currency, "potion": potion, "mypos": mypos}
            f["attributes"] = attributes
            f.sync()
            f.close()
            print("Game saved")
            break
        elif action == "save3" or action == "SAVE3" or action == "Save3":
            f = shelve.open("save3.dat")
            attributes = {"Name": Name, "Race": Race, "Class": Class, "Weapon": Weapon, "Xp": Xp,
                          "Player_Lvl": Player_Lvl, "Currency": Currency, "potion": potion, "mypos": mypos}
            f["attributes"] = attributes
            f.sync()
            f.close()
            print("Game saved")
            break
________________________________________________________________________________________________________________________

        '''
title_screen()
