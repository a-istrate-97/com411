def pattern():
    sequences = {}
    sequences = {'Short Sequence':3, 'Medium Sequence':2, 'Long Sequence':1}
    return sequences

def display_keys(data):
    print("Keys:")
    for key in data.keys():
        print(key)

def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)

def display_items(data):
    print("Items:")
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    sequences = pattern()
    print("Dictionary:")
    print(sequences)
    print()
    display_keys(sequences)
    print()
    display_values(sequences)
    print()
    display_items(sequences)

if __name__ == "__main__":
    run()