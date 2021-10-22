def export(file_path, no):
    if no > 2:
        return print("We don't have that much time!")
    print("Exporting...")
    with open(file_path, "a") as file:
        for bots in range(no):
            print("Please enter the bot id:")
            bot_id = input()
            print("Please enter the bot name:")
            bot_name = input()
            print("Please enter the bot paint:")
            bot_paint = input()
            data = f"{bot_id},{bot_name},{bot_paint}\n"
            file.write(data)
    print("Done!")

def run():
    export("exported_bots.csv", 2)

if __name__ == "__main__":
    run()

