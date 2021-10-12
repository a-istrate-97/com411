print("What strange markings do you see?")
strange_markings = input()
print("")
print("Identifying...")
print("")
for count in range(0, len(strange_markings), 1):
    print(f"index {count}", strange_markings[count])
print("")
print("Done!")