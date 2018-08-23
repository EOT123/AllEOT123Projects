# The PickPocket
# Probably Really Inefficient Way Of Doing.
# By Efrain
innocent_villager = ['Pear', 'Harp', 'Wallet', 'Pet', 'Hat']
pickpocket = []
print("Pear=1, Harp=2, Wallet=3, Pet=4, Hat=5")
while True:
    steal = input("Enter The Index Number Of Item To Pickpocket: ")
    print("_____________________________________________")
    if steal == '1':
        pickpocket.append('Pear')
        innocent_villager.remove('Pear')
        print("PickPocket Inv: {}".format(pickpocket))
        print("Innocent Villager Inv: {}".format(innocent_villager))
        print("_____________________________________________")
    elif steal == '2':
        pickpocket.append('Harp')
        innocent_villager.remove('Harp')
        print("PickPocket Inv: {}".format(pickpocket))
        print("Innocent Villager Inv: {}".format(innocent_villager))
        print("_____________________________________________")
    elif steal == '3':
        pickpocket.append('Wallet')
        innocent_villager.remove('Wallet')
        print("PickPocket Inv: {}".format(pickpocket))
        print("Innocent Villager Inv: {}".format(innocent_villager))
        print("_____________________________________________")
    elif steal == '4':
        pickpocket.append('Pet')
        innocent_villager.remove('Pet')
        print("PickPocket Inv: {}".format(pickpocket))
        print("Innocent Villager Inv: {}".format(innocent_villager))
        print("_____________________________________________")
    elif steal == '5':
        pickpocket.append('Hat')
        innocent_villager.remove('Hat')
        print("PickPocket Inv: {}".format(pickpocket))
        print("Innocent Villager Inv: {}".format(innocent_villager))
        print("_____________________________________________")
    else:
        print("Not An Item")
        print("_____________________________________________")

