from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
turtle.colormode(255)
# tim.shape("arrow")
# tim.width(15)
tim.speed("fastest")

#  This is creating square
# for _ in range(4)
#     tim.forward(100)
#     tim.right(90)
#

# This is creating dashed line.
# for _ in range(15 ):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

# This is the creation of different shape with different colors.
# colors = ['blue','forest green','yellow','tomato','dark red','dark slate blue','saddle brown']

# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)
#
# for draw_shape_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(draw_shape_n)


def RGB_color():
     r = random.randint(0,255)
     g = random.randint(0,255)
     b = random.randint(0,255)
#
#     # set python tuples not to change data
     random_color = (r, g, b)
#
     return random_color
#
#
# # This is creating a random walk
# directions = [0,90,180,270]
# for _ in range(300):
#     tim.color(RGB_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))




# This is creation multiple circle.
radius = 100
tim.screen.bgcolor('black')
tim.pensize(2)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(RGB_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()



