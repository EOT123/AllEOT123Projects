import turtle  # imports the turtle library
import random  # imports the rankdom library

scr = turtle.Screen()  # goes into turtle library and calls screen function
trt = turtle.Turtle()  # creates turtle


colors = ["red", "blue", "pink", "yellow", "green", "brown", "black", "white", "light blue", "dark red", "purple",
          "magenta", "tan", "orange"]


def little_draw():
    scr.tracer(10, 0)
    myx = random.randrange(-360, 360)
    myy = random.randrange(-360, 360)
    randsize = random.randrange(50, 100)
    color = random.choice(colors)
    trt.goto(myx, myy)  # sends turtle to random x and y
    trt.begin_fill()
    trt.circle(randsize)
    trt.color(color)
    trt.end_fill()


def big_draw():
    scr.tracer(500, 0)
    for variable_ok in range(100, 200):
        myx = random.randrange(-200, 200)
        myy = random.randrange(-200, 200)
        randsize = random.randrange(50, 100)
        color = random.choice(colors)
        trt.goto(myx, myy)  # sends turtle to random x and y
        trt.begin_fill()
        trt.circle(randsize)
        trt.color(color)
        trt.end_fill()


def clear():
    trt.clear()


scr.listen()  # readies screen events
scr.update()  # refreshes the screen
scr.onkey(little_draw, "a")
scr.onkey(big_draw, "w")
scr.onkey(clear, "c")

scr.mainloop()  # keeps screen looping
