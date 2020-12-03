MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffe": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffe": 24
        },
        "cost": 2.5
    },
    "capuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffe": 24
        },
        "cost": 3.0
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffe": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    # returns the total calculated from coins inserted
    print("Please insert coins.")
    total = int(input("How many 20 cents coins?: "))* 0.20
    total += int(input("How many 50 cents coins?: "))* 0.50
    total += int(input("How many 1 euros coins?: "))* 1
    total += int(input("How many 2 euros coins?: "))* 2
    return total

def is_transaction_succesfull (money_recieved, drink_cost):
    """return true when the payment is accepted or false if money is insuffient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffe (drink_name, order_ingredients):
    # dedcut the required ingredients from the resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")    


is_on = True
while is_on:
    choice = input("What do you like? (expresso/latte/capuccino): ")
    if choice == "off":
        is_on = False 
    elif choice == "report":
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml ")
        print(f"Coffe: {resources['coffe']}g ")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesfull(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])
