'''
Higher Order Functions are the functions which can take other functions as arguments
'''
from turtle import Turtle, Screen

tim = Turtle()

screen= Screen()



def move_forwards():
    tim.forward(10)



screen.listen()
screen.onkey(key ="space",fun = move_forwards)
screen.exitonclick()
