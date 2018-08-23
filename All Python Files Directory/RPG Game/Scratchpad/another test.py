# Python Text RPG
# Name

import sys
import os
import time


screen_width = 100

""" Player Setup """


class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


myPlayer = player()

""" Title Screen """


def title_screen_selection():
    option = input("> ")
    if option.lower() == "play":
        setup_game()  # placeholder
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please Enter A Valid Command")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def title_screen():
    print('###########################')
    print('# Welcome To The Text RPG #')
    print('###########################')
    print('          - Play -         ')
    print('          - Help -         ')
    print('          - Quit -         ')
    title_screen_selection()


def help_menu():
    print('###########################')
    print('# Welcome To The Text RPG #')
    print('###########################')
    print('- Use Up, Down, Left, Right To Move -')
    print('- Type Your Commands To Do Them -')
    print('- Use "Look" To Inspect Something -')
    print('- Good Luck And Have Fun! -')
    title_screen_selection()


"""Map"""
"""
-------------
|a1|a2|a3|a4|
-------------
|b1|b2|b3|b4|
-------------
|c1|c2|c3|c4|
-------------
|d1|d2|d3|d4|
-------------
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
                 }

zonemap = {
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
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: "",
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

}

"""Game Interactivity"""
"""
EX:
#######
#Apple#
#######
"""


def print_location():
    print('\n' + '#' * (4 + len(myPlayer.location)))
    print('# ' + myPlayer.location.upper() + '#')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + '#')
    print('\n' + '#' * (4 + len(myPlayer.location)))


def prompt():
    print("\n" + "==========================")
    print("What Would You Like To Do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown Action, Try Again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())


def player_move(myAction):
    ask = "Where Would You Like To Move To?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You Have Moved To The" + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You Have Already Exhausted This Zone.")
    else:
        print("You Can Trigger A Puzzle Here.")


"""Game Functionality"""


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # Here Handle If Puzzles Have Been Solved, Boss Defeated, Explored Everything, Etc.


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
    question2 = "What Is Your Role?\n"
    question2added = "(You Can Choose Warrior, Mage, Or Priest)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You Are Now A " + player_job + ".\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You Are Now A " + player_job + ".\n")

    """Player Stats"""
    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'priest':
        self.hp = 60
        self.mp = 60

    """Introduction"""
    question3 = "Welcome, " + player_name + " The " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "Welcome To This Fantasy World!\n"
    speech2 = "I hope It Greets You Well!\n"
    speech3 = "Just Make Sure You Don't Get Too Lost...\n"
    speech4 = "Heheheh...\n"
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
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    print("###################")
    print("# Let's Start Now #")
    print("###################")
    main_game_loop()


title_screen()
