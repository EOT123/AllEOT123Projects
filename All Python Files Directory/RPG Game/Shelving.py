import shelve

f = shelve.open("save.dat")
Currency = 2
potion = "3"
f["attributes"] = {"Currency": Currency, "potion": potion}
f.sync()
f.close()

f = shelve.open("save.dat")
attributes = f["attributes"]
f.close()
Currency = attributes["Currency"]
print(Currency)
