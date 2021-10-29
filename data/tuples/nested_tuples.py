def steps():
    likelihoods = []
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods

def run():
    likelihoods = steps()
    good_steps = []
    bad_steps = []
    for index in range(len(likelihoods)):
        nest = likelihoods[index]
        if nest[1] >= 50:
            bad_steps.append(nest[0])
        else:
            good_steps.append(nest[0])
    print(f"Good steps: {len(good_steps)}, bad steps: {len(bad_steps)}")

if __name__ == "__main__":
    run()