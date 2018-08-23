import turtle
myScreen = turtle.Screen()
trt002 = turtle.Turtle()

def mover():
    trt002.forward(100)
    trt002.right(90)
    myScreen.update()

myScreen.listen()
myScreen.onkeypress(mover, "a")
myScreen.onkeypress(mover, "w")
myScreen.onkeypress(mover, "s")
myScreen.onkeypress(mover, "d")

myScreen.mainloop()