print("How far are we from the cave?")
howfar = int(input())

for i in range(howfar, 0, -1):
    print(f"{i} steps remaining")

print("We have reached the cave!")