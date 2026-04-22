print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    pizza_cost = 12
elif size == "M":
    pizza_cost = 20
else:
    pizza_cost = 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        pizza_cost += 2
    elif size == "M":
        pizza_cost += 3
    else:
        pizza_cost += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    pizza_cost += 1

print (f"your final bill is: ${pizza_cost}")