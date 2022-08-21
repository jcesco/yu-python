from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiate objects
menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    items = menu.get_items()
    selection = input(f"Would you like an {items}? ")

    if selection == 'off':
        is_on = False
    elif selection == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(selection)
        if menu_item is None:
            continue

        if coffee_machine.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_machine.make_coffee(menu_item)


