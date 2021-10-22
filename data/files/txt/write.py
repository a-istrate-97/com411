def search(file_path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(file_path, "rt") as file:
        for line in file:
            if line.startswith("Section"):
                sections = sections + line # + "\n"
            else:
                books = books + line # + "\n"
    print("Done!")
    #print(f"{sections}\n\n{books}")
    data = sections + "\n\n" + books
    return data

def save(file_path, stored_string):
    print("Saving...")
    with open(file_path, "w") as file:
        file.write(stored_string)
    print("Done!")

def run():
    data = search("books.txt")
    save("section-books.txt", data)

run()


