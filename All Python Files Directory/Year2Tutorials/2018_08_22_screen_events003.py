import turtle

scr = turtle.Screen()
trt = turtle.Turtle()
scr.tracer(10, 0)
scr.title("Graphics")


def go_again():
    x = scr.numinput("Circle Size", 'Enter Size 1-10', 0, 1, 10)
    trt.penup()
    trt.goto(-200, 200)
    trt.write("Pattern Size")
    trt.goto(0, 0)
    trt.pendown()
    x = x * 10
    littlex = x * .618


def draw_star(size, color):
    angle = 160
    trt.fillcolor(color)
    trt.begin_fill()
    for side in range(5):
        trt.forward(size)
        trt.right(angle)
        trt.forward(size)
        trt.right(72 - angle)
    trt.end_fill()
    return


go_again()
draw_star(100, "blue")
scr.mainloop()


