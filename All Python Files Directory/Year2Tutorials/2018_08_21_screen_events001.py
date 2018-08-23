import turtle  # imports the turtle library
import random  # imports the rankdom library

scr = turtle.Screen()  # goes into turtle library and calls screen function
trt = turtle.Turtle()  # creates turtle


def little_draw():
    scr.tracer(10, 0)
    myx = random.randrange(-360, 360)
    myy = random.randrange(-360, 360)
    randsize = random.randrange(50, 100)
    trt.goto(myx, myy)  # sends turtle to random x and y
    trt.begin_fill()
    trt.circle(randsize)
    trt.end_fill()


scr.listen()  # readies screen events
scr.update()  # refreshes the screen
scr.onkey(little_draw, "a")

scr.mainloop()  # keeps screen looping
