import turtle

timi = turtle.Turtle()
timi.shape('turtle')
forward = 10

for spiral in range(0, 19):
    timi.right(60)
    timi.forward(forward)
    forward += 10

turtle.done()
