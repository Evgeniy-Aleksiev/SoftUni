import turtle

timi = turtle.Turtle()
timi.shape("turtle")
timi.color("pink")
timi.shapesize(5)
timi.pensize(4)


for turtleGraphics in range(0, 4):
    timi.left(30)
    timi.forward(200)
    timi.left(120)
    timi.forward(200)
    timi.left(120)
    timi.forward(200)

    timi.left(-30)
    timi.penup()
    timi.backward(50)
    timi.pendown()
    timi.backward(100)
    timi.penup()
    timi.forward(150)
    timi.pendown()
    timi.left(30)


turtle.done()