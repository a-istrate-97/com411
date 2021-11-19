import csv
import matplotlib.pyplot as plt

def read_data():
    data_dict = {}
    with open("temps.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        header = next(csv_reader)
        week1_list = []
        week2_list = []
        for row in csv_reader:
            week1_list.append(row[0])
            week2_list.append(row[1])
        data_dict = {header[0]:week1_list, header[1]:week2_list}
    return data_dict

def run():
    data = read_data()
    temperatures = []
    days = range(1,8)
    for value in data.values():
        temperatures.append(value)
    fig, axs = plt.subplots(2, 1, sharex='col')
    axs[0].plot(days, temperatures[0])
    axs[1].plot(days, temperatures[1])
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    run()

