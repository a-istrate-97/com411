import matplotlib.pyplot as plt


def read_data(file_path):
    data_list = []
    with open(file_path) as file:
        data = file.read()
        line = data.split('\n')
    return line


def run():
    data = read_data("temps.txt")
    figs, axs = plt.subplots(1, 2)
    x = range(1, 8)
    axs[0].plot(data)
    axs[1].bar(x, data)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run()