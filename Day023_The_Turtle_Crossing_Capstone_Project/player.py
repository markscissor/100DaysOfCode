from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_front(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        y_current = self.ycor()
        x_new = self.xcor() - MOVE_DISTANCE
        self.goto(x_new, y_current)

    def move_right(self):
        y_current = self.ycor()
        x_new = self.xcor() + MOVE_DISTANCE
        self.goto(x_new, y_current)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
