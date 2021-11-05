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

def display_menu():
    print("""
Please select one of the following options (1, 2, 3, 4, 5 or 6):
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
[5] Display the number of survivors per age group
[6] Search passenger by name
""")
    return int(input())

def display_passenger_names():
    print("The names of the passengers are...")
    for index in range(len(records)):
        nest = records[index]
        passenger_name = nest[3]
        print(passenger_name)

def display_num_survivors():
    num_survived = 0
    for index in range(len(records)):
        nest = records[index]
        survival_status = int(nest[1])
        if survival_status == 1:
            num_survived = num_survived + 1
    print(f"{num_survived} passengers survived")

def display_passengers_per_gender():
    females = 0
    males = 0
    for index in range(len(records)):
        nest = records[index]
        if nest[4] == "female":
            females = females + 1
        elif nest[4] == "male":
            males = males + 1
    print(f"females: {females}, males: {males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for index in range(len(records)):
        nest = records[index]
        if nest[5] != "" and nest[5].isdigit():
            age = int(nest[5])
            if age < 18:
                children = children + 1
            elif age < 65:
                adults = adults + 1
            elif age > 64:
                elderly = elderly + 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")

def display_survivors_per_age_group():
    children = 0
    s_children = 0
    adults = 0
    s_adults = 0
    elderly = 0
    s_elderly = 0
    for index in range(len(records)):
        nest = records[index]
        survived = int(nest[1])
        if nest[5] != "" and nest[5].isdigit() and survived == 1:
            age = int(nest[5])
            if age < 18:
                s_children = s_children + 1
            elif age < 65:
                s_adults = s_adults + 1
            elif age > 64:
                s_elderly = s_elderly + 1
        if nest[5] != "" and nest[5].isdigit():
            age = int(nest[5])
            if age < 18:
                children = children + 1
            elif age < 65:
                adults = adults + 1
            elif age > 64:
                elderly = elderly + 1
    print(f"children: {s_children}/{children}, adults: {s_adults}/{adults}, elderly: {s_elderly}/{elderly}")

def search_passenger_by_name():
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

def run():
    load_data("titanic.csv")
    selected_option = display_menu()
    print(f"You have selected the option: {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    elif selected_option == 6:
        search_passenger_by_name()
    else:
        print("Error! option not recognised!")

if __name__ == "__main__":
    run()
