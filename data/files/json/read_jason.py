import json

def read(file_path):
    with open(file_path) as file:
        data = json.load(file)
        city = data["city"]
        population = data["population"]
        bots = data["bots"]
        print(f"City Name: {city}")
        print(f"Population: {population}")
        for bot in bots:
            bot_name = bot["name"]
            bot_stats = bot["stats"]
            print(f"{bot_name} has the following stats: {bot_stats}")

def run():
    read("robocity.json")

if __name__ == "__main__":
    run()