def display_chars(path, characters):
    with open(path) as file:
        print(f"The first {characters} characters are:")
        partial_data = file.read(characters)
        print(partial_data)

def display_line(path):
    with open(path) as file:
        print("The first line is:")
        line = file.readline().strip()
        print(line)

def display_text(path):
    with open(path) as file:
        print("The full text is:")
        data = file.read()
        print(data)

def run():
    display_chars("library.txt", 12)
    print()
    display_line("library.txt")
    print()
    display_text("library.txt")

run()