from machine_data import MENU, resources, COINS, profits


# TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

def give_options():
    """give the different options of coffee to the user to choose"""
    user_chosen = ""
    while (user_chosen != "espresso" and user_chosen != "latte" and user_chosen != "cappuccino"
           and user_chosen != "report" and user_chosen != "off"):
        user_chosen = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return user_chosen


def report(resources):
    """Show the report to the user"""
    for item in resources:
        if item == "coffee":
            print(f"{item.capitalize()}: {resources[item]}g")
        else:
            print(f"{item.capitalize()}: {resources[item]}ml")
    print(f"Money: ${profits["money"]}")


def check_resources(type_of_coffee, resources):
    """Check if there is enough resources to make the coffee"""
    for item in MENU[type_of_coffee]["ingredients"]:
        if resources[item] < MENU[type_of_coffee]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return "not enough"

    return "enough"


def processing_coins():
    """Check the total amount of money inserted by the user"""
    print("Please insert coins")
    total_inserted = 0
    for types in COINS:

        coins_inserted = ""
        while not coins_inserted.isnumeric():
            coins_inserted = input(f"How many {types}?:")

        total_inserted += round(float(coins_inserted) * COINS[types], 3)
        print(f"total: ${total_inserted}")
    return total_inserted


def checking_transaction(money_inserted, type_of_coffe):
    """Check if the total amount of money inserted by the user is enough to buy the selected coffe"""
    change = money_inserted - MENU[type_of_coffe]["cost"]
    if change > 0:
        print(f"Here is ${change} in change.")
        return "make a coffee"
    elif change == 0:
        return "make a coffee"
    else:
        print(f"""${money_inserted} is not enough to buy a {type_of_coffe} that costs {MENU[type_of_coffe]["cost"]}.
         Your money will be refunded.""")
        return "do not make a coffee"


def coffe_machine():
    status = "on"
    while status == "on":
        type_of_coffe = give_options()

        # a. Check the user’s input to decide what to do next.
        # b. The prompt should show every time action has completed, e.g. once the drink is
        # dispensed. The prompt should show again to serve the next customer.

        # TODO: 2. Print report of all coffe machine resources
        if type_of_coffe == "report":
            report(resources)
            # TODO 7. Turn off the Coffee Machine by entering “ off ” to the prompt.
            # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
            # the machine. Your code should end execution when this happens.
        elif type_of_coffe == "off":
            status = "off"

        # TODO: 3. Check resources are sufficient to make drink order
        elif check_resources(type_of_coffe, resources) == "enough":
            # TODO: 4. Process coins.
            money_inserted = processing_coins()

            # TODO: 5. Check transaction successful
            if checking_transaction(money_inserted, type_of_coffe) == "make a coffee":
                # TODO: 6. Make coffe
                for item in resources:
                    resources[item] -= MENU[type_of_coffe]["ingredients"][item]

                profits["money"] += MENU[type_of_coffe]["cost"]
                print(f"Here is your {type_of_coffe} ☕. Enjoy!")


coffe_machine()
