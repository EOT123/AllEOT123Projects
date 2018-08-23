# Getting Warmer
# WIP
import random
number = '50'

print(number)
while True:
    warm = input("Try To Find The Number: ")
    if warm != int:
        print("Invalid")
    elif warm == number:
        print('{} Is HOT'.format(warm))
        print("Yay I Guess")
    elif warm <= '60':
        print("Warm")
    elif warm >= '40':
        print("Warm")
    else:
        print('{} Is Cold'.format(warm))
