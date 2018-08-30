import random


for numofrolls in range(20):
    randomdiceroll = random.randrange(1, 7)
    print(randomdiceroll)
    if randomdiceroll >= 5:
        print("lethal damage")
    elif randomdiceroll >= 3:
        print("pretty good")
    else:
        print("not enough damage")
    print("----------------------")
