from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="make  you bet", prompt="Which turtle will win the race? Enter the color : ")
colors = ["red","orange","yellow","green","blue", "purple"]
all_turtle = []

y_position = [-70,-40,-10,20,50,80]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won. The winning color is {winning_color}.")

            else:
                print(f"You've lost. The winning color is {winning_color}.")
        random_race = random.randint(0,10)
        turtle.forward(random_race)


















screen.exitonclick()
