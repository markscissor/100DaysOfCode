from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self, ball_speed):
        if self.ycor() <= 240:
            new_y = self.ycor() + 20 + ball_speed * 2
            self.goto(self.xcor(), new_y)

    def go_down(self, ball_speed):
        if -240 <= self.ycor():
            new_y = self.ycor() - 20 - ball_speed * 2
            self.goto(self.xcor(), new_y)
