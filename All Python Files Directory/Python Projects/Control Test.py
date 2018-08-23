import turtle
trt=turtle.Turtle()
scr=turtle.Screen()

turtle.listen(xdummy=None, ydummy=None)

scr.bgcolor("black")
trt.color("white")

def w():
    trt.seth(90)
    trt.forward(10)

scr.onkeypress(w, "w")
scr.onkey(w, "w")

def s():
    trt.seth(270)
    trt.forward(10)

scr.onkeypress(s, "s")
scr.onkey(s, "s")

def a():
    trt.seth(0)
    trt.forward(10)

scr.onkeypress(a, "a")
scr.onkey(a, "a")

def d():
    trt.seth(180)
    trt.forward(10)

scr.onkeypress(d, "d")
scr.onkey(d, "d")

scr.listen()

scr.mainloop()