def observed():
    observations = []
    for i in range(7):
        print("Please enter an observation")
        obs = input()
        observations.append(obs)
    return observations

def run():
    print("Counting observations...")
    obs = observed()
    obset = set()
    for index in range(len(obs)):
        count = obs.count(obs[index])
        tuple = (obs[index], count)
        obset.add(tuple)
    for data in obset:
        print(f"{data[0]} observed {data[1]} times.")

if __name__ == "__main__":
    run()