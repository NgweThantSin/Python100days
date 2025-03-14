from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score_update()
        self.hideturtle()


    def score_update(self):
        self.clear()
        self.write(f"Score = {self.score} : High Score = {self.high_score}", align="center", font=("Arial", 20, "normal"))



    def increase_score(self):
        self.clear()
        self.score += 1
        self.score_update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.write("Game over",align="center", font=("Arial", 24, "Normal"))
