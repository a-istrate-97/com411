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

def run():
    load_data("titanic.csv")
    selected_option = display_menu()
    print(f"You have selected the option: {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    else:
        print("Error! option not recognised!")

if __name__ == "__main__":
    run()
