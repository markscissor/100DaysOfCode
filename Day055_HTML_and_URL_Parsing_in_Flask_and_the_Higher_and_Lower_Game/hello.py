from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasized(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
@make_emphasized
@make_underlined
def bye():
    return 'Bye!'


@app.route('/<name>')
def greeet(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
