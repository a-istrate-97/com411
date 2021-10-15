def climb_ladder(remaining, crossed):
    if remaining > crossed:
        print("Still some way to go!")
    elif remaining < crossed:
        print("We are almost there!")
    else:
        print("You took as many steps as there are remaining")

climb_ladder(5,2)
climb_ladder(2,5)