from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)


def Counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def Clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def Clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="f", fun= move_forward )
screen.onkey(key="s", fun= move_backward)
screen.onkey(key="a", fun=Counter_clockwise)
screen.onkey(key="d", fun=Clockwise)
screen.onkey(key="c", fun=Clear)



screen.exitonclick()