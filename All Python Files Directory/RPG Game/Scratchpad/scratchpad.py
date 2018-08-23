Xp = 0
Player_Lvl = 0
Xp_Next_Lvl = 40


def xp():
    global Xp
    global Player_Lvl
    global Xp_Next_Lvl
    while Xp >= Xp_Next_Lvl:
        Player_Lvl += 1
        Xp = Xp - Xp_Next_Lvl
        Xp_Next_Lvl = round(Xp_Next_Lvl * 1.2)
    print("Xp {}".format(Xp))
    print("Player_Lvl {}".format(Player_Lvl))
    print("Xp_Next_Lvl {}".format(Xp_Next_Lvl))


def xp_cheat():
    global Xp
    Xp += 100
    print("Xp {}".format(Xp))
    print("Player_Lvl {}".format(Player_Lvl))
    print("Xp_Next_Lvl {}".format(Xp_Next_Lvl))


def prompt():
    global Xp
    print("\n" + "__________________________")
    print("What Would You Like To Do?")
    action = input("> ")
    acceptable_actions = ['level', 'xp', 'xp_up']
    while action.lower() not in acceptable_actions:
        print("Unknown Action, Try Again.\n")
        action = input("> ")
    if action.lower() in ['xp', 'level']:
        xp()
    elif action.lower() in ['xp_up']:
        xp_cheat()


def main_game_loop():
    while True:
        prompt()


main_game_loop()
