# import random
# print(dir(random))
#
# x = random.randrange(1, 100)
# print(x)

import turtle

scr = turtle.Screen()
scr.screensize(720, 720)

trt = turtle.Turtle()
trt.seth(0)
trt.color("red")
trt.begin_fill()
trt.circle(100)
trt.end_fill()
trt.back(100)
trt.color("blue")
trt.begin_fill()
trt.circle(200)
trt.end_fill()

scr.mainloop()
