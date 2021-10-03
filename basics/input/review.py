#Present new feature
print("Beep has been recently updated with a square root function")
print("Beep wants you to put his new update to the test")
#Ask user for a whole number
print("Please enter a whole number")
#Get the number as an integer
number = int(input())
#Calculate square root
square_root = float(number ** 0.5)
#Format the result (to be displayed later)
square_root_formatted = "{:.2f}".format(square_root)
print()
#Reply to the user
print(f"Square root of {number} is {square_root}")
print()
#Ask user for his/her name
print("Beep wants to know what is your name")
#Get user name
name = input()
#Tell user about Beep's gratefulness
print(f"Beep is very grateful for your help {name}")
#Ask user to write a short review
print("Beep asks you to write down a 3-5 line review of his new software update")
print("Please begin to write line 1")
line_1 = input()
print("Please begin to write line 2")
line_2 = input()
print("Please begin to write line 3")
line_3 = input()
print("Thank you for your review")
#Present the review to the user
print("Beep will now send this review back to his developers")
print("This is how the review looks:")
print()
print("|---------------------------------------------------------------------|")
print("|                            Review letter                            |")
print("|---------------------------------------------------------------------|")
print("|\tTo: Dev Team")
print("|")
print(f"|\tBeep has helped me find out the square root of {number}")
print(f"|\tHe instantly gave me the answer, {square_root_formatted}, I am very impressed")
print(f"|\t{line_1}")
print(f"|\t{line_2}")
print(f"|\t{line_3}")
print("|---------------------------------------------------------------------|")
print(f"| Best Regards, {name}")
print("|---------------------------------------------------------------------|")