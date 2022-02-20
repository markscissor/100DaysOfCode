# Solve different problem worlds at https://reeborg.ca/reeborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()
r_count = 0
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
        r_count = 0
    elif r_count >= 3 and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
        r_count += 1
    else:
        turn_left()
