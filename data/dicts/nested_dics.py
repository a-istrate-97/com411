def short_pattern():
    pattern = {}
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern

def medium_pattern():
    pattern = {}
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern

def long_pattern():
    pattern = {}
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern

def run():
    print("Analysing patterns...")
    short_sequence = short_pattern()
    medium_sequence = medium_pattern()
    long_sequence = long_pattern()
    dictionary = {
        "short_sequence": short_sequence,
        "medium_sequence": medium_sequence,
        "long_sequence": long_sequence
    }
    for key, value in dictionary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    run()
