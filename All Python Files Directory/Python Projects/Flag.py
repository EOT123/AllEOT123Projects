#importing modules
from turtle import Turtle
from turtle import *

#Setting up variables
unVar1 = 25
unVar2 = 100
unVar3 = 90
unVar4 = 150
unVar5 = -30
unVar6 = 75
unVar7 = 50
screen = Screen() # create the screen

#first part in making the turtle move
turtle = Turtle()
t = Turtle() # create the first turtle
t2 = Turtle() # create the second turtle
screen.onscreenclick(turtle.goto) # set up the callback for moving the first turtle

#defining shapes and objects
def drawSquare(t , xPrime, yPrime, sideLength):
    t.up()
    t.hideturtle()
    t.goto(xPrime, yPrime)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(sideLength)
        t.left(90)
    t.end_fill()
def drawRectangle(t, x2, y2, sideLength1, sideLength2):
    t.up()
    t.hideturtle()
    t.goto(x2, y2)
    t.setheading(270)
    t.down()
    for count in range(2):
        t.forward(sideLength1)
        t.left(90)
        t.forward(sideLength2)
        t.left(90)
    t.end_fill()
def drawTank():
    t.pencolor("black")
    t.fillcolor("gray")
    t.begin_fill()
    tire1 = drawRectangle(t, int("10"), unVar1, unVar6, int("30")) #Tire
    t.begin_fill()
    tire2 = drawRectangle(t, int("110"), unVar1, unVar6, int("30"))    #Tire
    t.begin_fill()
    tire3 = drawRectangle(t, int("110"), unVar2, unVar6, int("30"))  #Tire
    t.begin_fill()
    tire4 = drawRectangle(t, int("10"), unVar2, unVar6, int("30"))   #Tire
    t.pencolor("gray")
    t.fillcolor("black")
    t.begin_fill()
    bodyTank = drawRectangle(t, int("20"), unVar3, int("130"), int("110"))
    t.begin_fill()
    gunTank = drawRectangle(t, int("65"), unVar4, int("100"), int("20"))   #Gun
    t.begin_fill()
    exhaustTank = drawRectangle(t, int("50"), unVar5, int("20"), int("10"))
    t.fillcolor("red")
    t.begin_fill()
    turretTank = drawSquare(t, int("50"), unVar7, int("50"))  #Turret
    t.end_fill()
drawTank()
screen.mainloop() # start everything running