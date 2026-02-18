from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(500,400)

is_race_on=False

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions =[-70,-40,-10,20,50,80]

turtles=[]

for turtle_index in range (0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x =-230,y=y_positions[turtle_index])
    turtles.append(tim)

if user_bet:
    is_race_on =True

while(is_race_on):

    for turtle in turtles:
        if turtle.xcor()> 230:
            winning_color=turtle.pencolor()
            if winning_color== user_bet:
                print("You won")
            else:
                print("Better Luck Next Time")
            is_race_on= False


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()