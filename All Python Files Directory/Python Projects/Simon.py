import random
import collections
tries = 4

guess = 0
possible_words = [['b', 'u', 's', 't', 'a'], ['b', 'a', 'n', 'a', 'n', 'a'], ['o', 'r', 'a', 'n', 'g', 'e'],
                  ['a', 'p', 'p', 'l', 'e']]
start = input("Would you like to play Yes or No")
while start == 'yes' or start == 'Yes' or start == "YES":
    word_chooser = random.choice(possible_words)
    player_word = [] * len(word_chooser)
    print(word_chooser)
    print(len(word_chooser), "letters")
    while player_word != word_chooser:
        guess = input("What letter do you think it is.")
        if word_chooser.count(guess) > 1 :
            player_word.append(guess)
            print("bep")
        if guess in word_chooser:
            player_word.append(guess)
            print("Yes")
            print(player_word)
        if guess not in word_chooser:
            print("Nope")
            tries = tries - 1
        if tries == 0:
            print("You tried to many times")
            break
    if player_word == word_chooser:
        start = input("Would you like to play Yes or No")
while start == "No" or start == 'no' or start == 'No':
    print("Okay Bye")
    break
