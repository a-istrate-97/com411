#Print question 1
print("What is your name human?")
#Get answer 1 as a string variable
human_name = str(input())
print("")
#Print question 2
print("How old are you (in years)?")
#Get answer 2 as an integer variable
human_age = int(input())
print("")
#Print question 3
print("How tall are you (in meters)?")
#Get answer 3 as a float variable
human_height = float(input())
print("")
#Print question 4
print("How much do you weigh (in kilograms)?")
#Get answer 4 as an integer
human_weight = int(input())
print("")
#Calculate BMI
human_bmi = human_weight / (human_height ** 2)
#Create a new variable to format the human_bmi float
human_bmi_formatted = "{:.2f}".format(human_bmi)
#Print answer
print(f"{human_name} you are {human_age} years old and your bmi is {human_bmi_formatted}.")
