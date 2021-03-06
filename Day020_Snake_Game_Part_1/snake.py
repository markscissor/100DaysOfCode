from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.size = 3
        self.direction = 0
        self.create_body()

    def create_body(self):
        for i in range(self.size):
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("gold")
            turtle.penup()
            turtle.prev_x = 0
            turtle.prev_y = 0
            x_start = -i * 20
            turtle.goto(x_start, 0)
            self.segments.append(turtle)

    def move(self):
        for idx, seg in enumerate(self.segments):
            seg.prev_x = seg.xcor()
            seg.prev_y = seg.ycor()

            if idx == 0:
                seg.setheading(self.direction)
                seg.forward(20)
            else:
                seg.goto(self.segments[idx - 1].prev_x, self.segments[idx - 1].prev_y)

    def move_up(self):
        if not self.direction == 270:
            self.direction = 90
        print("move up")

    def move_down(self):
        if not self.direction == 90:
            self.direction = 270
        print("move down")

    def move_left(self):
        if not self.direction == 0:
            self.direction = 180
        print("move left")

    def move_right(self):
        if not self.direction == 180:
            self.direction = 0
        print("move right")
