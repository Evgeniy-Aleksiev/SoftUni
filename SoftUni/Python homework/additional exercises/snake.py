import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Aleksiev")
wn.bgcolor("black")                     # Background color
wn.setup(width=600, height=600)         # Size of the screen
wn.tracer(0)                            # Turn off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)                           # Animation speed like module
# head.shapesize(0.5)
head.shape("square")
head.color("green")                       # Snake Head colour
head.penup()
head.goto(0, 0)                         # The snake is going to start in the center
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake segments
segments = []

# Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High score: 0", align="center", font=("Courier", 24, "normal"))


# Function                              # Snake move by 20 pixels in the coordinate
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)             # y = head.ycor()

    if head.direction == "down":
        head.sety(head.ycor() - 20)             # y = head.ycor()

    if head.direction == "left":
        head.setx(head.xcor() - 20)             # x = head.xcor()

    if head.direction == "right":
        head.setx(head.xcor() + 20)             # x = head.xcor()

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score} High score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check for collision with the food
    if head.distance(food) < 20:               # 20 pixels
        # Move the food to random spot: x = coordinate(-290, 290), y = coordinate(-290, 290)
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("dark green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorter the delay
        delay -= 0.00

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score} High score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # Move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()
            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write(f"Score: {score} High score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)               # The speed of the snake


wn.mainloop()