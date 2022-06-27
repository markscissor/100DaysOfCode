import math
import random
from flask import Flask
app = Flask(__name__)

target = -1


@app.route('/')
def guess():
    global target
    target = math.floor(random.random() * 9)
    view = f"<h1>Guess a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif' style='display: block;'>"
    for _ in range(10):
        view = view + f"<a href='/{_}'>" + \
            "<h1 style='display: inline; padding: 17px;'>" + \
            f"{_}</h1></a>"
    return view


@app.route('/redirect')
def redirect():
    global target
    view = f"<h1>Guess a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif' style='display: block;'>"
    for _ in range(10):
        view = view + f"<a href='/{_}'>" + \
            "<h1 style='display: inline; padding: 17px;'>" + \
            f"{_}</h1></a>"
    return view


@app.route('/<num>')
def check(num):
    global target
    number = int(num)
    if number == target:
        view = f"<h1 style='color: green'>You found me!</h1>" \
            "<img src='https://media.giphy.com/media/oCO02sFyanXFF68LHW/giphy.gif' >" \
            "<div style='display: block;'><a href='/'>NEW GAME</a></div>"
    elif number > target:
        view = f"<h1 style='color: red'>Too high, try again!</h1>" \
            "<img src='https://media.giphy.com/media/TiuShTf3ehYZi/giphy.gif' >" \
            "<div style='display: block;'><a href='/redirect'>BACK</a></div>"
    else:
        view = f"<h1 style='color: red'>Too low, try again!</h1>" \
            "<img src='https://media.giphy.com/media/JSjjpay0cZmtuSh7NJ/giphy.gif' >" \
            "<div style='display: block;'><a href='/redirect'>BACK</a></div>"
    return view


if __name__ == '__main__':
    app.run(debug=True)
