def sum_weights(bop_weight, beep_weight):
    return bop_weight + beep_weight
def calc_avg_weight(bop_weight, beep_weight):
    return (bop_weight + beep_weight) / 2
def run():
    print("Please enter Beep's weight")
    beep_weight = int(input())
    print("Please enter Bop's weight")
    bop_weight = int(input())
    print("Do you want the sum or the average of these 2?")
    user_input = input()
    if user_input == "sum":
        sum = sum_weights(bop_weight, beep_weight)
        print(f"The sum is {sum}")
    elif user_input == "average":
        avg = calc_avg_weight(bop_weight, beep_weight)
        print(f"The average is {avg}")
    else:
        print(f"Invalid response")
run()