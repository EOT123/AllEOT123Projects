f = "fizz"
b = "buzz"

for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print(i)
        print(f + b)
    elif i % 3 == 0:
        print(i)
        print(f)
    elif i % 5 == 0:
        print(i)
        print(b)
# complete
