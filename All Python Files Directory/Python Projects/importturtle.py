import turtle  # imports the entire turtle library or module - do importing first

myScreen = turtle.Screen()  # uses the turtle library, calls the screen function and name it myScreen
trt001 = turtle.Turtle()  # uses the turtle library calls the turtle function and names it trt001
trt002 = turtle.Turtle()  # uses the turtle library calls the turtle function and names it trt002

myScreen.tracer(1, 2)  # Tells the screen to draw very fast 10 means fastest 0 means no delay
trt002.pencolor("red")  # sets pencolor to red for trt002
trt002.pensize(3)
trt001.seth(0)  # points trt001 to the left
trt001.forward(200)  # moves turtle forward 200
trt002.seth(180)  # points the turtle right
trt002.forward(200)  # moves turtle forward 200
trt001.right(98)
trt001.forward(100)
trt001.left(123)
trt001.fd(49)  # fd = forward
trt002.right(276)
trt002.fd(100)

myScreen.update()

myScreen.mainloop()
