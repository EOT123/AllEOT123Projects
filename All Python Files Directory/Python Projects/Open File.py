openthis = input("print the name of the file you want to open  ")

with open(openthis) as f:
    print(f.read())

print(f.name)
print(f.mode)
