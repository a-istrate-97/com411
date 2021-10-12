print("How many mountains should I display?")
number = int(input())
print("")
print("Displaying...")
print("")
for mountains in range(number):
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\
  """)
print("")
print("Done!")