def directions():
    directions = []
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction (0,1,2 or 3):")
    dir = directions()
    for index in range(len(dir)):
        print(f"{index}: {dir[index]}")
    user_input = int(input())
    return dir[user_input]

def run():
    route = []
    print("Working out escape route...")
    for index in range (5):
        route.append(menu())
    print(f"Escape route: {route}")

if __name__ == "__main__":
    run()
