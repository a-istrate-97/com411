print("Please enter a sequence:")
sequence = input()
print()
print("Please enter the character for the marker:")
marker = input()
p1 = None
p2 = None
for position in range(0, len(sequence), 1):
    letter = sequence[position]
    if letter == marker:
        if(p1 == None):
            p1 = position
        else:
            p2 = position
print(f"The distance between the markers is {p2}")


