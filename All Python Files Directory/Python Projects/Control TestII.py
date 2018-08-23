import turtle
trt = turtle.Turtle()
scr = turtle.Screen()

trt.tracer(4, 0)

turtle.listen(xdummy=None, ydummy=None)

scr.bgcolor("black")
trt.color("white")


def wkey():
    trt.seth(90)
    trt.forward(10)


def skey():
    trt.seth(270)
    trt.forward(10)


def akey():
    trt.seth(180)
    trt.forward(10)


def dkey():
    trt.seth(0)
    trt.forward(10)


def space():
    trt.clear()

scr.onkeypress(space, "space")
scr.onkeypress(wkey, "w")
scr.onkeypress(skey, "s")
scr.onkeypress(akey, "a")
scr.onkeypress(dkey, "d")

scr.listen()

scr.mainloop()
