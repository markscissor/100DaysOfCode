from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto((0, 280))
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"{self.player_1_score} - Player 1 | Player 2 - {self.player_2_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def point(self, player_num):
        if player_num == 1:
            self.player_1_score += 1
            self.refresh()
        elif player_num == 2:
            self.player_2_score += 1
            self.refresh()
