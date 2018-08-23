import turtle

scr = turtle.Screen()
scr.tracer(8)
little_t = turtle.Turtle()
big_t = turtle.Turtle()
for variablename in range(1, 20):
    little_t.pensize(5)
    little_t.fd(100)
    little_t.rt(98)
    little_t.circle(20)
    big_t.color("blue")
    big_t.fd(100)
    big_t.rt(97)
scr.mainloop()
