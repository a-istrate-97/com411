import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(1, 1)


def animate(frame):
    global ax
    ax.cla()
    ax.set_xlim(0+frame, 720+frame)
    ax.set_ylim(-1, 1)
    x = range(0+frame, 720+frame)
    y = []
    for number in x:
        x_in_radians = math.radians(number)
        y.append(math.sin(x_in_radians))
    ax.plot(x, y)


def run():
    global fig
    some_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)
    plt.tight_layout()
    plt.show()


run()
