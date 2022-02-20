from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        start_dir = random.randint(1, 2)
        self.reset_ball(start_dir)
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.hit_count = 0

    def bounce(self, axis):
        if axis == 'x':
            self.setheading(360 - self.heading())

        elif axis == 'y':
            if 180 < self.heading() < 360:
                self.setheading(540 - self.heading())
            elif 0 < self.heading() < 180:
                self.setheading(180 - self.heading())
            self.hit_count += 1
            print(self.hit_count)
        print(f"Bouncing to direction: {self.heading()}")

    def move(self):
        self.forward(10)

    def reset_ball(self, player_dir):
        initial_hlist = [
            [],
            [random.randint(105, 165), random.randint(175, 255)],
            [random.randint(15, 75), random.randint(285, 345)],
        ]
        self.hit_count = 0
        self.goto((0, random.randint(-270, 270)))
        s = random.choice(initial_hlist[player_dir])
        self.setheading(s)
