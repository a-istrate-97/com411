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

    #test
    #print(headings)


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

if __name__ == "__main__":
    run()
