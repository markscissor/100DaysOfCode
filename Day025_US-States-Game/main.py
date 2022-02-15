import turtle
from turtle import Turtle, Screen
import pandas

FONT = ('Courier', 8, 'normal')

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = Turtle()
writer.penup()
writer.hideturtle()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    title = f"{len(guessed_states)}/50 States Guessed"
    answer_state = screen.textinput(title=title, prompt="What's another state's name?")
    if not answer_state:
        pass
    elif answer_state.title() == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        data_out = pandas.DataFrame(missing_states)
        data_out.to_csv("missed_states.csv")
        break
    else:
        answer_state = answer_state.title()
    data = pandas.read_csv("50_states.csv")
    if answer_state in data['state'].tolist():
        coordinates = (int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        writer.goto(coordinates)
        writer.write(arg=answer_state, align="center", font=FONT)
        guessed_states.append(answer_state)

    # for state in data['state'].tolist():
    #     coordinates = (int(data[data.state == state].x), int(data[data.state == state].y))
    #     writer.goto(coordinates)
    #     writer.write(arg=state, align="center", font=FONT)

screen.exitonclick()
