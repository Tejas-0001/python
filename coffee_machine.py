flavours = ["espresso","latte","cappuccino"]

recipe = {
    "espresso":{
        "price": 1.50,
        "water": 50,
        "coffee": 18,
        "milk":0
    },
    "latte":{
        "price":2.50,
        "water": 200,
        "coffee":24,
        "milk":150
    },
    "cappuccino":{
        "price":3.00,
        "water" : 250,
        "coffee" : 24,
        "milk" : 100
    }
}

resource={
    "water":300,
    "milk":200,
    "coffee":100
}

coin = {
    "penny":0.01,
    "nickel":0.05,
    "dime":0.10,
    "quarter":0.25
}

def report():
    print(resource)

def resource_sufficient(choice):
    if resource["water"] >= recipe[choice]["water"] and resource["milk"] >= recipe[choice]["milk"] and resource["coffee"] >= recipe[choice]["coffee"]:
        return 1
    else:
        return 0

def process_coins(p,n,d,q):
    amt = p*coin["penny"]+n*coin["nickel"]+d*coin["dime"]+q*coin["quarter"]
    return amt

def transaction(choice,amt):
    balance = amt - recipe[choice]["price"]
    if balance >= 0:
        print("coffee is being dispensed")
        if balance >0:
            print(f"here's the change{balance}")
        return 1
    else:
        print("money not sufficient!!")
        print(f"returning money :{amt}")
        return 0

def brew(choice):
    resource["water"]-= recipe[choice]["water"]
    resource["milk"]-=recipe[choice]["milk"]
    resource["coffee"]-=recipe[choice]["coffee"]

state = "on"
while state == "on":
    coffee = input("what would you like (latte/espresso/cappuccino)\n")
    if coffee == "off":
        break
    if coffee == "report":
        report()
        continue

    if resource_sufficient(coffee):
        print("Enter the money")
        for item in recipe:
            print(f"{item} price= {recipe[item]['price']}")
        p = int(input("enter no of penny\n"))
        n = int(input("enter no of nickel\n"))
        d = int(input("enter no of dime\n"))
        q = int(input("enter no of quarter\n"))

        amount = process_coins(p,n,d,q)
        if transaction(coffee,amount):
            brew(coffee)
            print("your coffee is ready to be picked up")
    else:
        print("insufficient resource for coffee")

