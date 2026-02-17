from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")

timmy_the_turtle.color("red")

#Drawing the square
for i in range(0,4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


for i in range(0,10):
    timmy_the_turtle.backward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.backward(10)
    timmy_the_turtle.pendown()





screen = Screen()
screen.exitonclick()