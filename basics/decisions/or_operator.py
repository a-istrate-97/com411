print("What type of adventure should I have?")
type = input()
if type == "scary" or type == "short":
    print("Entering the dark forest!")
elif type == "safe" or type == "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")