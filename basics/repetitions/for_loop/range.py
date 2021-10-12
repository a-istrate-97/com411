print("What level of brightness is required?")
brightness= int(input())

print("Adjusting brightness...")
print("")
for i in range(2, brightness + 1, 2):
    print(f"Beep's brightness level: {'*' * i}")
    print(f"Bop's brightness level: {'*' * i}")
    print("")
print("")
print("Adjustments complete!")