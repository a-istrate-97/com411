# ask the user for the age
print("Please enter your age")

#read the user's response
age = int(input())

#check if the user is an adult and display an appropriate message
if age >= 18:
    print("You are an adult")
    print("Because you are 18 years old or greater")
else:
    print("You are not an adult")
    print("Because you are 17 years old or less")