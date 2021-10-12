print("Which of the following do you think is a better sport?"
      " \"Football\" or \"MMA\"?")
sport = input().lower()
if sport == "football":
    print("Have you ever been to a football match?")
    answer = input().lower()
    if answer == "yes":
        print("Very nice! You are a true football fan")
    elif answer == "no":
        print("You are not a super fan then!")
    else:
        print("Beep didn't understand your answer")
elif sport == "mma":
    print("Is Conor McGregor your favorite fighter?")
    answer1 = input().lower()
    print("Have you ever been to an MMA fight?")
    answer2 = input().lower()
    if answer1 == "yes" and answer2 == "yes":
        print("I'm guessing you have seen him fight live!")
    elif answer1 == "no" and answer2 == "yes":
        print("You might have seen Conor fight live")
    elif (answer1 == "yes" and answer2 == "no") or (answer1 == "no" and answer2 == "no"):
        print("You are not a super fan then!")
    else:
        print("Beep didn't understand your answer")
else:
    print("Beep doesn't recognise this sport...")