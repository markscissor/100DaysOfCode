from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


def main():
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()

    while True:
        command = input(f"What would you like? {menu.get_items()}: ").lower()

        if command == 'off':
            break
        elif command == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(command)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


main()
