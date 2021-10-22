def export(file_path, no):
    if no > 2:
        return print("We don't have that much time!")
    print("Exporting...")
    with open("output.csv", "a") as file:
        for bots in range(no):
            print("Please enter the bot id:")
            bot_id = input()
            print("Please enter the bot name:")
            bot_name = input()
            print("Please enter the bot paint:")
            bot_paint = input()
    file.write("{bot_id},{bot_name},{bot_paint}")
    print("Done!")

def run():
    export("exported_bots.csv", 2)

if __name__ == "__main__":
    run()

