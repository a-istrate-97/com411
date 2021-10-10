print("Please enter a number")
number = int(input())

i = 0
factorial = 1

while i < number:
    i = i + 1
    factorial = factorial * i

print(f"The factorial is {factorial}")