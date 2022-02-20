import turtle
from turtle import Screen
from snake import Snake
import time


snake = Snake()
game_on = True


def exit_game():
    global game_on
    game_on = False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 2022")
screen.tracer(0)
screen.listen()
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")
screen.onkey(exit_game, "e")


while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


screen.exitonclick()
