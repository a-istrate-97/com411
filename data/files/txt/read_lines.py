def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        line = file.readline()
        for line in file:
            print(f"Looked in {line}")
    print("...Done!")

def run():
    search("library.txt")

if __name__ == "__main__":
    run()

