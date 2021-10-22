import random
print("Please enter the minimum value:")
min_value = int(input())
print()
print("Please enter the maximum value:")
max_value = int(input())
print()
random_number = random.randrange(min_value, max_value)
print(f"I am thinking of a number between {min_value} and {max_value}. Can you guess what it is?")
print()
print("Please enter a number:")
guessed_correctly = False
while guessed_correctly == False:
    guess = int(input())

    if guess == random_number:
        print("Congratulations! You guessed the correct answer!")
        guessed_correctly = True
    elif guess < random_number:
        print("Guess higher")
        print("Try again:")
    else:
        print("Guess lower")
        print("Try again:")
print()
print("Game over!")