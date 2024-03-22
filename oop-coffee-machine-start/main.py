from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
items = drinks.get_items()
chef = CoffeeMaker()
cashier = MoneyMachine()


while 1:
    print("Welcome to coffee shop")
    print("what will you like to have today?")
    print(items)
    choice = input("enter coffee name\n").lower()
    if choice == "report":
        chef.report()
        continue
    if choice == "profit":
        cashier.report()
        continue
    if choice == "off":
        break
    if choice == "latte" or "espresso" or "cappuccino":
        available = drinks.find_drink(choice)
        if available is not None:
            if chef.is_resource_sufficient(available):
                print(f"Amount to be paid : {available.cost}")
                if cashier.make_payment(available.cost):
                    chef.make_coffee(available)
                else:
                    continue
            else:
                continue
        else:
            continue
print("machine switched off")