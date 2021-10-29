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


def run():
    load_data("titanic.csv")



if __name__ == "__main__":
    run()
