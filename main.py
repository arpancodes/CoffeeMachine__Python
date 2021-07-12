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
    "money": 0
}


def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def update_resources(coffee):
    for key in coffee["ingredients"]:
        resources[key] -= coffee["ingredients"][key]
    resources["money"] += coffee["cost"]


def process_payment(coffee):
    print(f"You need to pay ${coffee['cost']}")
    quarters = int(input("Enter no of quarters: ")) * 0.25
    dime = int(input("Enter no of dime: ")) * 0.10
    nickles = int(input("Enter no of nickels: ")) * 0.05
    pennies = int(input("Enter no of pennies: ")) * 0.01
    total = quarters + nickles + dime + pennies
    if total < coffee["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print("Your coffee is ready! Enjoy")
        update_resources(coffee)
        if total > coffee["cost"]:
            print(f'Here is ${round(total - coffee["cost"], 2)} dollars in change.')


def process_coffee(coffee_type):
    print(f"Getting {coffee_type} ready.")
    coffee_req = MENU[coffee_type]
    coffee_resources = coffee_req["ingredients"]
    for key in coffee_resources:
        if coffee_resources[key] > resources[key]:
            print(f"Insufficient {key}")
            return
    process_payment(coffee_req)


isMachineOn = True
while isMachineOn:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        isMachineOn = False
    elif choice == "report":
        print_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        process_coffee(choice)
    else:
        print(f"Couldn't recognise {choice}")