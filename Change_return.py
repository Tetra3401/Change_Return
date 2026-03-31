import random
# Change return program
# When given a number it will return the change back in dollars and coins
randomCost = round(random.random() * 200, 2)
print(f"Your item costs $ {randomCost:.2f}")
payment = round(float(input("Type out an amount to pay: $")), 2)
#Convert to cents
changeTotal = round((payment - randomCost) * 100)

# Dollars
dollars = changeTotal // 100
changeTotal %= 100

# Quarters
quarters = changeTotal // 25
changeTotal %= 25

# Dimes
dimes = changeTotal // 10
changeTotal %= 10

# Nickels
nickels = changeTotal // 5
changeTotal %= 5

# Pennies
pennies = changeTotal


#Print the result
print()
print(f"You recieve:")
print(f"{dollars} dollars")
print(f"{quarters} quarters")
print(f"{dimes} dimes")
print(f"{nickels} nickels")
print(f"{pennies} pennies.")
