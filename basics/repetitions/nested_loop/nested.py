print("How many rows should I have?")
rows = int(input())
print()
print("How many columns should I have?")
columns = int(input())

print("Here I go:")

for count_rows in range(0, rows, 1):
    for count_columns in range(0, columns, 1):
        print(":-)", end ="")
    print()

print("Done!")