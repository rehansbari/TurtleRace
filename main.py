#This is a program I wrote in python to create a simple betting game
# The game uses the built in python turtle class
# The program will generate a set of ROYGBV turtles, ask the user to chose which turtle they think will win,
# then have the turtles move across the screen in a randomized fashion

import turtle
from turtle import Turtle, Screen
import random

#Starting values
is_race_on = False
STARTING_X = -240
STARTING_Y = -180

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "orange", "green", "purple", "yellow"]
turtles = []

#Function that creates turtles and sets them to their starting value (the left of the screen)
def create_turtles():
    global STARTING_Y
    global STARTING_X
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=STARTING_X, y=STARTING_Y)
        STARTING_Y += 60
        turtles.append(new_turtle)


create_turtles()

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} was the winning turtle")
            else:
                print(f"You lose {winning_color} was the winning turtle")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()