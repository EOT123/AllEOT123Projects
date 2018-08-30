import turtle  # imports the turtle library
import random  # imports the random library

scr = turtle.Screen()  # goes into turtle library and calls screen function
trt = turtle.Turtle()  # creates turtle
scr.bgcolor("black")  # changes background color
trt.hideturtle()  # hides turtle

colors = ["red", "blue", "pink", "yellow", "green", "brown", "white", "light blue", "dark red", "purple",
          "magenta", "tan", "orange"]  # a list of colors


def background_color():  # changes background color when "b" pressed
    color = random.choice(colors)  # random color
    scr.bgcolor(color)  # changes background to random color


def changing_background_color():  # flashing colors
    color = random.choice(colors)
    for variable_k in range(0, 100):
        scr.bgcolor(color)


def little_draw():  # draws a circle when "a" pressed
    scr.tracer(10, 0)  # draws fast
    myx = random.randrange(-360, 360)  # random x location
    myy = random.randrange(-360, 360)  # random y location
    randsize = random.randrange(50, 100)  # random size
    color = random.choice(colors)  # random color
    trt.penup()  # stops drawing
    trt.goto(myx, myy)  # sends turtle to random x and y
    trt.begin_fill()  # starts filling
    trt.circle(randsize)  # random circle size
    trt.color(color)  # random turtle color
    trt.end_fill()  # stops filling
    trt.pendown()  # starts drawing


def big_draw():  # draws 100 circles when "w" pressed
    scr.tracer(10, 0)  # draws fast
    for variable_ok in range(0, 100):  # draws 100 circles
        myx = random.randrange(-200, 200)  # random x location
        myy = random.randrange(-200, 200)  # random y location
        randsize = random.randrange(50, 100)  # random circle size
        color = random.choice(colors)  # random color
        trt.penup()  # stops drawing
        trt.goto(myx, myy)  # sends turtle to random x and y
        trt.begin_fill()  # starts filling
        trt.circle(randsize)  # random circle size
        trt.color(color)  # random turtle color
        trt.end_fill()  # stops filling
        trt.pendown()  # starts drawing


def draw_star():  # draws a star when "q" pressed
    scr.tracer(10, 0)  # draws fast
    angle = random.randrange(120, 180)  # random angle in range 120 to 180
    color = random.choice(colors)  # random color
    myx = random.randrange(-200, 200)  # random x location
    myy = random.randrange(-200, 200)  # random y location
    trt.penup()  # stops drawing
    trt.begin_fill()  # starts filling
    for side in range(5):  # draws 5 times
        trt.color(color)   # random turtle color
        trt.forward(100)  # goes forward 100
        trt.right(angle)  # goes right random angle
        trt.forward(100)  # goes forward 100
        trt.right(72 - angle)  # goes right 72 - random angle
    trt.end_fill()  # stops filling
    trt.goto(myx, myy)  # goes to random x and y
    trt.pendown()  # starts drawing


def clear():  # clears drawings when "c" pressed
    trt.clear()  # clears drawings


scr.listen()  # readies screen events
scr.update()  # refreshes the screen
scr.onkey(background_color, "b")  # activates background color when "b" pressed
scr.onkeypress(changing_background_color, "n")  # dont look at screen
scr.onkeyrelease(changing_background_color, "n")  # crazy flashing colors
scr.onkey(little_draw, "a")  # activates little draw when "a" pressed
scr.onkey(big_draw, "w")  # activates big draw when "w" pressed
scr.onkey(draw_star, "q")  # activates draw star when "q" pressed
scr.onkey(clear, "c")  # activates clear when "c" pressed

scr.mainloop()  # keeps screen looping
