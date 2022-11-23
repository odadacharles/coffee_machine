from menu_resources import resources, MENU

# initialize variables
machine_on = True


def print_report():
    """Returns the quantities of ingredients and cash available"""
    print(f"Water:{resources['water']} ml")
    print(f"Milk:{resources['milk']} ml")
    print(f"Coffee:{resources['coffee']} gms")
    print(f"Money: ${resources['money']}")


def prompt():
    """ Asks the user for an entry which can be an order, a report, or switching machine off"""
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == "report":
        print_report()
        return True
    if order == "off":
        return False
    else:
        check_quantities(order)
        return True


def check_quantities(drink_choice):
    """ Processes the customers order; keeping track of resources used and money collected """
    if drink_choice == "espresso":
        if resources['water'] >= MENU["espresso"]["ingredients"]["water"] and \
                resources['coffee'] >= MENU["espresso"]["ingredients"]["coffee"]:
            if coin_counter(MENU["espresso"]["cost"]):
                resources['water'] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                resources["money"] += MENU["espresso"]["cost"]
                print("Here is your espresso ☕")

        else:
            resource_check("espresso")
    elif drink_choice == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and \
                resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and \
                resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            if coin_counter(MENU["latte"]["cost"]):
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["money"] += MENU["latte"]["cost"]
                print("Here is your Latte ☕ ")

        else:
            resource_check("latte")
    elif drink_choice == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and \
                resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and \
                resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            if coin_counter(MENU["cappuccino"]["cost"]):
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["money"] += MENU["cappuccino"]["cost"]
                print("Here is your cappuccino ☕ ")

        else:
            resource_check("cappuccino")


def resource_check(drink):
    if drink == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, not enough water")
        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, not enough coffee")
    elif drink == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry, not enough water")
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, not enough milk")
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, not enough coffee")
    elif drink == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, not enough water")
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, not enough milk")
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry, not enough coffee")


def coin_counter(cost):
    """ Checks if customers money is sufficient for transaction/order"""
    print("Please insert coins")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    cash_total = 0.25*quarters+0.1*dimes+0.05*nickels+0.01*pennies
    if cash_total < cost:
        print("Insufficient funds for transaction!")
        return False
    elif cash_total == cost:
        return True
    elif cash_total > cost:
        print(f"Here is {cash_total-cost} in change!")
        return True


while machine_on:
    if not prompt():
        machine_on = False
