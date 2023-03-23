from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align='center', font=('Arial', 24, 'normal'))

    def score_counter(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align='center', font=('Arial', 24, 'normal'))
        