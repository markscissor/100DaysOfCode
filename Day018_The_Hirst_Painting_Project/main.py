# import colorgram as c
#
#
# rgb_colors = []
# colors = c.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as t
t.colormode(255)

color_list = [(241, 222, 86), (35, 98, 185), (86, 174, 218), (169, 67, 37), (217, 158, 84), (187, 16, 34),
              (173, 49, 85), (78, 108, 210), (225, 57, 103), (161, 163, 23), (166, 27, 17), (75, 176, 77),
              (232, 70, 44), (225, 123, 172), (125, 198, 117), (20, 55, 146), (59, 119, 64), (118, 226, 184),
              (71, 30, 43), (135, 216, 233), (238, 158, 217), (41, 172, 183), (29, 41, 84), (242, 175, 152),
              (162, 165, 235), (90, 30, 22)]

# 10x10 dots, 20 in size, 50 paces apart
tits = t.Turtle()
tits.hideturtle()
tits.speed("fastest")
tits.penup()
x_start = -250
y_start = -250
tits.setx(x_start)
tits.sety(y_start)

for _ in range(10):
    tits.setx(x_start)
    for _ in range(10):
        x, y = tits.position()
        # tits.pencolor(random.choice(color_list))
        tits.dot(20, random.choice(color_list))
        tits.setx(x + 50)
        # print(f"{x}_{y}")
    tits.sety(y + 50)


screen = t.Screen()
screen.exitonclick()
