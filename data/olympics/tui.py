def started(msg=""):
    print("-------------------------------------")
    print(f"Operation started: {msg}...\n")


def completed():
    print("Operation completed.")
    print("-------------------------------------")


def error(msg):
    print(f"Error! {msg}")


def menu():
    print(
    f"[years]     List unique years\n"
    "[tally]      Tally up medals\n"
    "[ctally]     Tally up medals for each team\n"
    "[exit]       Exit the program\n")
    selection = input()
    return selection


def display_medal_tally(tally):
    print(tally.items())


def display_team_medal_tally(team_tally):
    for key, value in team_tally.items():
        print(f"{key}\n{value}")


def display_years(years):
    for year in years:
        print(year)

