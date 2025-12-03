import sys

in_file = sys.argv[1]

with open(in_file, "r") as f:
    power_banks = f.readlines()

total_output_joltage = 0
max_joltage = 0
second_joltage = 0


for bank in power_banks:
    joltages = list(map(int, list(bank.strip())))
    
    # find max value and its index
    max_joltage = max(joltages)
    i_max = joltages.index(max_joltage)

    # check that it is not at the end of the list
    # if it is, take the second largest value as the max
    # and the old max as the second value
    if i_max == len(joltages) - 1:
        second_joltage = max_joltage
        max_joltage = max(joltages[:-1])
        i_max = joltages.index(max_joltage)
    # look up the largest value after the max value in the list
    else:
        second_joltage = max(joltages[i_max+1:])       


    #print(f"Joltage: {max_joltage}{second_joltage}")

    output = str(max_joltage) + str(second_joltage)

    total_output_joltage += int(output)


print(f"Output: {total_output_joltage}")
