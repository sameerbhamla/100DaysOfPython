print("welcome to the tip calculator")
total = input("What was the total bill? ")
tipPercent = input("What percentage tip would you like to give? 10, 12, or 15? ")
tipPercent = (float(tipPercent) + 100) / 100
numOfPeople = input("How many people to split the bill? ")

amtPerPerson = (float(total) / int(numOfPeople)) * tipPercent
amtPerPerson = round(amtPerPerson,2)
print(f"Each person should pay: ${amtPerPerson}")