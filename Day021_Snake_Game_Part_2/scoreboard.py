from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 270)
        self.print_score()

    def add_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"SCORE : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
