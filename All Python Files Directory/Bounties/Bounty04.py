#Bounty04-Clickable Raindrops
import turtle

scr = turtle.Screen()
trt01 = turtle.Turtle()

trt01.shape("circle")

trt01.stamp()
scr.onscreenclick(trt01.clearstamps())
for i in range(1, 7):
    trt01.shapesize(i)
    trt01.color("blue")


scr.mainloop()
