print("Towards which direction should I paint (up, down, left or right)?")
direction = input()

if direction == "up":
    print("I am painting in the upward direction!")
elif direction == "down":
    print("I am painting in the downard direction!")
elif direction == "left":
    print("I am painting in the leftward direction!")
elif direction == "right":
    print("I am painting in the rightward direction!")
else:
    print("I don't recognize this direction")