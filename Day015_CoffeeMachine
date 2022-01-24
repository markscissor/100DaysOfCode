MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


# TODO: 1. Print report of all coffee machine resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# TODO: 2. Check if resources are sufficient
def enough_rss(drink):
    for rss in MENU[drink]['ingredients']:
        if resources[rss] < MENU[drink]['ingredients'][rss]:
            print(f"Sorry there is not enough {rss}.")
            return False
    return True


# TODO: 3. Process coins
# TODO: 4. Check if transaction is successful
def process_coins(drink):
    price = MENU[drink]['cost']
    coins = 0
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    coins += quarters * 0.25
    coins += dimes * 0.1
    coins += nickles * 0.05
    coins += pennies * 0.01

    if coins >= price:
        return coins - price
    else:
        print("Sorry that's not enough money. Money refunded.")
        return -1


# TODO: 5. Make coffee
def make_coffee(drink):
    for rss in MENU[drink]['ingredients']:
        resources[rss] -= MENU[drink]['ingredients'][rss]
    resources['money'] += MENU[drink]['cost']


def main():
    while True:
        command = input(" What would you like? (espresso/latte/cappuccino): ").lower()

        if command == 'report':
            report()
        elif command in MENU:
            if enough_rss(command):
                change = process_coins(command)
                if change >= 0:
                    make_coffee(command)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {command} ☕. Enjoy!")
        elif command == 'off':
            break
        else:
            print('Invalid input.')


main()
