import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((-360, 0))
paddle2 = Paddle((360, 0))
ball = Ball()
game_over_msg = Turtle()
scoreboard = Scoreboard()
game_is_on = True


def exit_game():
    global game_is_on
    game_is_on = False


def game_over(msg):
    global game_is_on
    game_is_on = False
    game_over_msg.color("white")
    game_over_msg.goto((0, 0))
    game_over_msg.write(arg=f"GAME OVER. {msg}", move=False, align=ALIGNMENT, font=FONT)


def pad_w():
    paddle1.go_up(ball.hit_count)


def pad_s():
    paddle1.go_down(ball.hit_count)


def pad_up():
    paddle2.go_up(ball.hit_count)


def pad_dw():
    paddle2.go_down(ball.hit_count)


screen.listen()
screen.onkey(pad_w, "w")
screen.onkey(pad_s, "s")
screen.onkey(pad_up, "Up")
screen.onkey(pad_dw, "Down")
screen.onkey(exit_game, "e")
bounce_cooldown_y = 0
bounce_cooldown_x = 0

while game_is_on:
    time.sleep(0.03 + 0.07 * (1 / (ball.hit_count + 1)))
    screen.update()
    ball.move()
    if bounce_cooldown_y > 0:
        bounce_cooldown_y -= 1
    # print(bounce_cooldown_y)
    if bounce_cooldown_x > 0:
        bounce_cooldown_x -= 1
    # print(bounce_cooldown_x)

    # Detect if ball hit paddle
    if ball.distance(paddle1.position()) < 50 and -350 <= ball.xcor() <= -340 or ball.distance(paddle2.position()) < 50 and \
            350 >= ball.xcor() >= 340:
        if bounce_cooldown_y == 0:
            ball.bounce('y')
            bounce_cooldown_y = 20
    elif ball.ycor() >= 280 or ball.ycor() <= -280:
        if bounce_cooldown_x == 0:
            ball.bounce('x')
            bounce_cooldown_x = 20

    # Detect if ball out of bounce
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            scoreboard.point(1)
            ball.reset_ball(1)
        else:
            scoreboard.point(2)
            ball.reset_ball(2)

    if scoreboard.player_1_score >= 10:
        game_over("Player 1 wins!")
    elif scoreboard.player_2_score >= 10:
        game_over("Player 2 wins!")

screen.exitonclick()
