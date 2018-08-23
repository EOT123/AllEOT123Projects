import random
Player_Hand = []
Shuffled_Deck = []
Deck = []
Suits = [" Of Spades", " Of Hearts", " Of Diamonds", " Of Clubs"]
Ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
Random_Card1 = random.choice(Ranks)
Random_Card2 = random.choice(Suits)
print("You Drew A " + Random_Card1 + Random_Card2)

for eot in Suits:
    newsuit = eot
    for ctj in Ranks:
        newrank = ctj
        newcard = "The {} of {}".format(ctj, eot)
        Deck.append(newcard)
print(Deck)

for d in Deck:
    print(d)

