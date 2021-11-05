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
Please select one of the following options (1, 2, 3 or 4):
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
[5] Display the number of survivors per age group
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
    else:
        print("Error! option not recognised!")

if __name__ == "__main__":
    run()
