import random
import webbrowser

print("_________________________________")
print("Guess The Number Busta")
print("_________________________________")
print("")
guess = -1
name = input("What Is Your Name Busta? ")
print("Hello Busta ... I mean " + name)
the_number = random.randint(0, 10)
while guess != the_number:
    guess = input("What Is Your Guess Busta / " + name)
    guessint = int(guess)
    if guessint < the_number:
        print("Too Low Busta")
    elif guessint > the_number:
        print("Higher Than Ryder Busta")
    else:
        print("That's Right Busta")
        print(guess)
        webbrowser.open("")
        break
print("You Good Busta")
