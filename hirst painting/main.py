import colorgram
from turtle import Turtle, Screen
import colorgram
import random
import turtle
tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()

# rgb_color = []
# colors = colorgram.extract('spot_art.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

color_list = [(238, 250, 245), (188, 18, 44), (244, 232, 62), (252, 236, 241), (210, 236, 242), (196, 74, 33), (218, 66, 107), (20, 124, 173), (196, 175, 18), (107, 182, 209), (14, 142, 88), (18, 166, 214), (210, 152, 93), (24, 39, 76), (186, 41, 61), (77, 174, 95), (36, 44, 111), (237, 230, 4), (214, 68, 50), (219, 129, 156), (124, 185, 119), (236, 164, 184), (6, 59, 39), (147, 208, 221), (9, 93, 54), (5, 85, 111), (160, 29, 28), (236, 171, 164), (163, 212, 177)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")



for dot_count in range(1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()