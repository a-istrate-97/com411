print("Program Started!")
print()
print("Please enter an ASCII code:")
code = abs(int(input()))
if code in range(33, 126):
    char = chr(code)
    print(f"The character represented by the ASCII code {code} is {char}")
else:
    print("Can't display this character")
print()
print("Program Ended!")