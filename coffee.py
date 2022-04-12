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
profit = 0 #돈의 금액이 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):         #리소스가 충분한가(주문 재료):
    """주문이 가능하면 참을 반환 재료가 부족하면 거짓을 반환"""
    for item in order_ingredients:
       if order_ingredients[item]>= resources[item]:  #주문재료의 아이템(물,우유,커피) 값을 나타냄>=리소스 아이템(물,우유,커피)
         print(f"Sorry there is not enough {item}.")
         return False    #재료가 충분하지 않으면 반복문을 멈춰야하니 False 반환
    return True          #재료가 충분할때 True 반환하여 반복문 계속 실행


def is_transaction_successful(money_received, drink_cost):#입력값은 거스름돈, 음료의 가격
    """사용자가 정상적으로 지불했을떄 참을 반환 , 지불금액이 부족할떄 거짓반환"""
    if money_received>=drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is many ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money.")
        return False



def process_coin():
    """총 금액을 계산하여 반환한다 """
    print("pleas insert coins.")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    """자판기에 있는 재료에서 필요한 재료의 양을 차감"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is {drink_name}")


is_on = True

while is_on:#3
    choice = input("What would you like? (espresso/latte/cappuccino): ")#1
    if choice == "off":#2
        is_on = False#4
    elif choice == "report":#5
       print(f"water: {resources['water']}ml",)
       print(f"milk: {resources['milk']}ml",)
       print(f"coffee: {resources['coffee']}g"),
       print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment = process_coin()   #지불 금액
           if is_transaction_successful(payment, drink["cost"]):
              make_coffee(choice, drink["ingredients"])
