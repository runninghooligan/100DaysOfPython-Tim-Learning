print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
print(bill)
print(tip)
print(people)
tip_total = bill * tip/100
tip_per_person = tip_total / people
print(tip_total)
pay_per_person = bill / people + tip_per_person
print(pay_per_person)
print(f"Each person should pay: {pay_per_person:.2f}")

