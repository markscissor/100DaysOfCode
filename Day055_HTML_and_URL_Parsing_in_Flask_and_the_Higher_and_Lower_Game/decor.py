# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        a = ""
        for idx, x in enumerate(args):
            if idx == 0:
                a = a + f"({x}"
            else:
                a = a + f", {x}"

        a = a + ")"

        print(f"You called {function.__name__}{a}")
        print(f"It returned: {function(*args)}")

    return wrapper

# Use the decorator 👇


@logging_decorator
def a_function(a, b, c):
    return a+b+c


a_function(1, 2, 3)
