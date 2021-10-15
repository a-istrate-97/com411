def display_ladder(steps):
    for step in range(steps):
        print("| |")
        print("***")

def create_ladder():
    print("How many steps remain?")
    steps_remaining = int(input())
    display_ladder(steps_remaining)

create_ladder()