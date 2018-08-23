import turtle
myxloc = 0
myyloc = 0

scr=turtle.Screen()
locations = [[0,0],[0,1],[0,2],[0,3]]
scr.listen()
while True:

    def moveleft():
        myxloc = myxloc -1
        print(myxloc,myyloc)
    def moveright():
        myxloc = myxloc + 1

print(myxloc, myyloc)
scr.onkey(moveleft,'a')
scr.onkey(moveleft,'d')


