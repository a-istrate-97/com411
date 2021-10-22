import csv

def extract(file_path):
    print("Extracting...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        names = ""
        for values in csv_reader:
            names = names + values[1] + "\n"
        print("Done! Extracted names are as follows:")
        print(names)

def run():
    extract("bots.csv")

if __name__ == "__main__":
    run()