from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.prev_h = []
        self.size = 3
        self.direction = 0
        self.head = None
        self.create_body()
        self.print_pos()

    def create_body(self):
        for i in range(self.size):
            self.add_segment((-i * 20, 0))

        self.head = self.segments[0]

    def add_segment(self, position):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.color("cyan")
        turtle.speed("fastest")
        turtle.penup()
        turtle.prev_x = None
        turtle.prev_y = None
        turtle.goto(position)
        self.segments.append(turtle)
        self.prev_h.append(turtle.heading())

    def print_pos(self):
        for segment in self.segments:
            print(segment.position())

    def extend_body(self):
        self.size += 1
        self.add_segment(self.segments[-1].position())

    def move(self):
        prev = self.prev_h
        self.prev_h = []
        for idx, seg in enumerate(self.segments):
            seg.prev_x = seg.xcor()
            seg.prev_y = seg.ycor()

            if idx == 0:
                seg.setheading(self.direction)
                seg.forward(20)
            else:
                seg.setheading(prev[idx - 1])
                seg.goto(self.segments[idx - 1].prev_x, self.segments[idx - 1].prev_y)

            self.prev_h.append(seg.heading())

    def move_up(self):
        if not self.direction == 270:
            self.direction = 90
        # print("move up")

    def move_down(self):
        if not self.direction == 90:
            self.direction = 270
        # print("move down")

    def move_left(self):
        if not self.direction == 0:
            self.direction = 180
        # print("move left")

    def move_right(self):
        if not self.direction == 180:
            self.direction = 0
        # print("move right")
