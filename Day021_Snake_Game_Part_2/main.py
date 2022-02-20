from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


snake = Snake()
food = Food()
scoreboard = Scoreboard()
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
    time.sleep(0.2)
    screen.update()
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend_body()

    # Detect collision with wall.
    x_head = snake.segments[0].xcor()
    y_head = snake.segments[0].ycor()
    if x_head > 280 or x_head < -280 or y_head > 280 or y_head < -280:
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        # print(snake.head.distance(segment))
        # if segment == snake.head:
        #     # print(f"head: {segment.position()}")
        #     pass
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
