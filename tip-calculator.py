# tip-calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bil? $"))
tip = int(input("How much tip you wanna give? 0%, 5%, 10% "))
people = int(input("How many people to split the bill? "))
finalbill = bill + (bill * (tip/100))
bill_per_person = (round(finalbill,2)/people)
print(f"Each person should pay: ${bill_per_person}")
