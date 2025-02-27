from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.adding_level()

    def adding_level(self):
        self.goto(-290,280)
        self.write(f"level: {self.level}", align="left", font=("Courier", 12, "normal"))

    def level_update(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))


