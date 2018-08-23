# Flip Flopper
'''
Flip = input("Input Something To Be Flipped: ")
Flip2 = Flip
print(Flip2)
'''
flip = input("Input Something To Be Flipped: ")


def change(input_str):
    return input_str[-1] + input_str[1:-1] + input_str[0]


print()
