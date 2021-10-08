print("What type of cover does the book have?")
cover = input()
if cover == "soft":
    print("Is the book perfect-bound?")
    answer = input()
    if answer == "yes":
        print()
        print("Soft cover, perfect bound books are very popular!")
    else:
        print()
        print("Soft covers with coils or stiches are great for short books")
elif cover == "hard":
    print()
    print("Books with hard covers can be more expensive!")
else:
    print()
    print("I don't recognize this type of book cover")