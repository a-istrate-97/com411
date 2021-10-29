def likelihood():
    likelihoods = ()
    likelihoods = (50, 38, 27, 99, 4)
    values = []
    values.append(min(likelihoods))
    values.append(max(likelihoods))
    return values

def run():
    values = likelihood()
    print(f"Minimum likelihood of falling: {values[0]}%")
    print(f"Maximum likelihood of falling: {values[1]}%")

if __name__ == "__main__":
    run()