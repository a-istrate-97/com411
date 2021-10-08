print("Please enter the first whole number.")
no1 = int(input())
print("Please enter the second whole number.")
no2 = int(input())
print("Please enter the third whole number.")
no3 = int(input())

oddnumbers = 0
evennumbers = 0

if no1 % 2 == 0:
    evennumbers = evennumbers + 1
else:
    oddnumbers = oddnumbers + 1
if no2 % 2 == 0:
    evennumbers = evennumbers + 1
else:
    oddnumbers = oddnumbers + 1
if no3 % 2 == 0:
    evennumbers = evennumbers + 1
else:
    oddnumbers = oddnumbers + 1

print()
print(f"There were {evennumbers} even and {oddnumbers} odd numbers")
