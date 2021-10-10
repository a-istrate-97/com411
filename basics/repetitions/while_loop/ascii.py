print("How many bars should be charged?")
bars = int(input())
charged_bars = 0

while charged_bars < bars:
    print(f"Charging: {'█ ' * charged_bars}")
    charged_bars += 1

print("The battery is fully charged.")