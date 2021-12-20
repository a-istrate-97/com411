def started(msg=""):
    print("-------------------------------------")
    print(f"Operation started: {msg}...\n")


def completed():
    print("Operation completed.")
    print("-------------------------------------")


def error(msg):
    print(f"Error! {msg}")


def menu():
    print(f"""Please select one of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    selection = input()
    return selection


def display_medal_tally(tally):
    print(tally.items())


def display_team_medal_tally(team_tally):
    for key, value in team_tally.items():
        print(f"{key}\n{value}")


def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)

