import matplotlib.pyplot as plt
import random


def data():
    paths = {}
    print("What type of line would you like? (\":\", \"--\" or \"-\")")
    line = input()
    print("What colour would you like? (r, g or b)")
    colour = input()
    print("What marker style would you like? (o, s or ^)")
    marker = input()
    paths = {"line": line, "colour": colour, "marker": marker}
    return paths


def generate():
    print("How many lines would you like to display?")
    lines = int(input())
    for line in range(lines):
        values = data()
        values2 = []
        for value in values.values():
            values2.append(value)
        string = values2[2] + values2[1] + values2[0]
        x = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
        y = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
        plt.plot(x, y, string)
        plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


if __name__ == "__main__":
    run()
