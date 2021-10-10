print("How many numbers should I sum up?")
numbers = int(input())
times_asked = 0
sum = 0

while times_asked < numbers:
    times_asked = times_asked + 1
    print(f"Please enter a number {times_asked} of {numbers}")
    temp_number = int(input())
    sum = sum + temp_number

print(f"The answer is {sum}")