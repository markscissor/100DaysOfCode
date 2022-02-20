import random
from turtle import Turtle, Screen


def distance_random():
    mov = random.randint(0, 10)
    return mov


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
turtle_list = []

for _ in turtle_colors:
    turtle_list.append(Turtle())

for idx, turtle in enumerate(turtle_list):
    turtle.color(turtle_colors[idx])
    turtle.shape("turtle")
    turtle.penup()
    y_start = -120 + idx * 40
    turtle.goto(-230, y_start)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() >= 220:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        turtle.forward(distance_random())


screen.exitonclick()
