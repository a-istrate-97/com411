print("Please enter a word")
word = input()

def function(display_method):
    if display_method == "box":
        print("-----------")
        print(f"[{word}")
        print("-----------")
    elif display_method == "lowercase":
        print(word.lower())
    elif display_method == "uppercase":
        print(word.upper())
    elif display_method == "mirrored":
        reversed_word = word [::-1]
        print(reversed_word)
        #   different method:
        #def display_mirrored(word):
        #mirrored = ""
        #for letter in reversed(word):
        #    mirrored += letter
        #print(f"{word} | {mirrored}")
    elif display_method == "repeat":
        print("How many times do you want the word to be repeated?")
        repeat = int(input())
        for i in range(repeat):
            print(word)
    else:
        print("Invalid display method")

def run():
    function("box")
    function("lowercase")
    function("uppercase")
    function("mirrored")
    function("repeat")

run()

