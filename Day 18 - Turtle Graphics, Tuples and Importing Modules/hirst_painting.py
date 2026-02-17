import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.colormode(255)  # Allow RGB values

# Create turtle
dot = turtle.Turtle()
dot.speed(0)
dot.hideturtle()
dot.penup()

# Optional: Hirst-style bright color palette
color_list = [
    (239, 71, 111),  # pink
    (255, 209, 102),  # yellow
    (6, 214, 160),  # green
    (17, 138, 178),  # blue
    (7, 59, 76),  # dark blue
    (255, 99, 72),  # coral
    (155, 93, 229),  # purple
    (255, 159, 28),  # orange
]

# Starting position
dot.setpos(-250, -250)

number_of_dots = 10  # 10x10 grid

for row in range(number_of_dots):
    for col in range(number_of_dots):
        dot.dot(40, random.choice(color_list))  # Draw dot (size, color)
        dot.forward(60)  # Space between dots

    dot.backward(60 * number_of_dots)
    dot.left(90)
    dot.forward(60)
    dot.right(90)

screen.exitonclick()
