menu = {
    "expresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee": 18,
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "coffee": 24,
            "milk"  : 150,
        },
        "cost" :  2.5,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "coffee": 24,
            "milk"  : 100,
        },
        "cost" : 3
    },
}

profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, that is not enough {item}.")
            return False
    return True

def process_coin():
    print("Please insert coins. ")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many nickels? : ")) * 0.05
    total += int(input("How many dime? : ")) * 0.10
    total += int(input("How many penny? : ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's {change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, That's not enough money. Money Refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}. Enjoy ")



is_continue = True

while is_continue :
    customer_order = input("What would you like? (espresso/latte/cappuccino) : ")
    if customer_order == "off":
        is_continue = False

    elif customer_order == "report":
        print(f"Water : {resources['water']}g")
        print(f"Milk : {resources['milk']}g")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money = ${profit}")

    else:
        drink = menu[customer_order]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(customer_order, drink["ingredients"])






