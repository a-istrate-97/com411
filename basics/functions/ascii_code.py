print("Program Started")
print()
print("Please enter a standard character:")
character = input()
if len(character) == 1:
    value = ord(character)
    print(f"The ASCII code for {character} is: {value}")
else:
    print("Please enter only one character")
print()
print("Program Ended!")