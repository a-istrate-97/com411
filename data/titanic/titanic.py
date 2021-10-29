import csv

records = []
headings = []

def load_data(file_path):
    #global headings
    #global records
    print("Loading data...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings.append(next(csv_reader))
        #headings = next(csv_reader)
        for values in csv_reader:
            records.append(values)
    print(f"Successfully loaded {len(records)} records.")
    print(f"Please enter a passenger name:")
    name = input()
    results = 0
    for index in range(len(records)):
        nest = records[index]
        if name in nest[3] and len(name) > 3:
           print(f"Found {nest[3]}")
           results = results + 1
    if results == 0:
        print(f"Couldn't find any passengers with variants of this name")
    elif results == 891:
        print("Invalid input")
    elif results > 1:
        print(f"Found {results} results")

def display_menu():
    print("""
Please select one of the following options (1, 2, 3 or 4):
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
""")
    return int(input())


def run():
    load_data("titanic.csv")
    selected_option = display_menu()
    print(f"You have selected the option: {selected_option}")

if __name__ == "__main__":
    run()
