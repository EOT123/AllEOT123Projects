# 11/7/17
# 10 To Win:Given 2 integers, a and b, return True if one if them is 10 or if their sum is 10.
import random

while True:
    int1 = random.randint(1, 10)
    int2 = random.randint(1, 10)
    Sum = int1 + int2
    if int1 == 10:
        print("({},{})-->True".format(int1, int2))
    elif int2 == 10:
        print("({},{})-->True".format(int1, int2))
    elif Sum == 10:
        print("({},{})-->True".format(int1, int2))
        break
    elif int2 != 10:
        print("({},{})-->False".format(int1, int2))
    elif int1 != 10:
        print("({},{})-->False".format(int1, int2))