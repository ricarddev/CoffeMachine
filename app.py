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
            print("Sorry ther is not enough {item}.")
            return False
    return True





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