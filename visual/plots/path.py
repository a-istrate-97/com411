import matplotlib.pyplot as plt


def coordinate():
    print("Please enter an x value")
    x = input()
    print("Please enter an y value")
    y = input()
    tuple_ = (x, y)
    return tuple_

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    values = [x_values, y_values]
    return values


def run():
    values = path()
    x = values[0]
    y = values[1]
    plt.plot(x, y, "ro--")
    plt.show()


if __name__ == "__main__":
    run()