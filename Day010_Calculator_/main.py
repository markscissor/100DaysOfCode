#Calculator
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

oper = """+
-
*
/"""

#Add
def add(n1, n2):
    """Adds two numbers and returns their sum.
    """
    return n1 + n2

#Subtract
def subtract(n1, n2):
    """Subtracts two numbers and returns their difference.
    """
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """Multiply two numbers and returns their product.
    """
    return n1 * n2

#Divide
def divide(n1, n2):
    """Divide two numbers and returns their quotient.
    """
    return n1 / n2


#Main program
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while True:
    cont_input = 'y'
    print(logo)
    num_1 = float(input("What's the first number?: "))
    print(oper)
    while cont_input == 'y':
        ops = input("Pick an operation: ")
        num_2 = float(input("What's the next number?: "))
        result = operations[ops](num_1, num_2)

        print(f"{num_1:0.1f} {ops} {num_2:0.1f} = {result:0.1f}")
        num_1 = result
        cont_input = input(f"Type 'y' to continue calculating with {result:0.1f}, or type 'n' to start a new calculation:\n").lower()
        if cont_input == 'n':
            clear()
    
    #Secret input to exit program
    if cont_input == 'x':
        break
