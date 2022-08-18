def print_report():
    for resource in resources.keys():
        print(f"{resource.title()}: {resources[resource]}")


def check_choice(choice):
    """This function calls out functions to check resources and money for a given drink"""
    if check_resources(MENU[choice]['ingredients']):
        if check_money(MENU[choice]['cost']):
            reduce_resources(MENU[choice]['ingredients'])
            increase_money(MENU[choice]['cost'])
            print(f"Here is your {choice} ☕, enjoy!")


def check_resources(drink_ingredients):
    """This function verifies there are sufficient ingredients for the selected drink"""
    for ingredient in drink_ingredients.keys():
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient} to make this drink.")
            return False
    return True


def check_money(price):
    """This function ensures the customer has paid enough for the selected drink"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

    if total >= price:
        change = total - price
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that is not enough money. Money refunded.")
        return False


def reduce_resources(drink_ingredients):
    """This function reduces the machine's resource count w.r.t. the drink made"""
    for ingredient in drink_ingredients.keys():
        resources[ingredient] = resources[ingredient] - drink_ingredients[ingredient]


def increase_money(price):
    resources["money"] += price


def coffee_machine():
    """This function runs the main coffee machine program"""
    selection = input("Would you like an espresso, latte or cappuccino? ")

    if selection == 'off':
        return False
    elif selection == 'report':
        print_report()
        return True
    else:
        check_choice(selection)
        return True


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
    "money": 0.00,
}

on = True
while on:
    on = coffee_machine()


