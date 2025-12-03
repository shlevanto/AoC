import sys

in_file = sys.argv[1]


with open(in_file, "r") as f:
    power_banks = f.readlines()


def find_number(battery_list, number_length, result=[]):
    """Finds the largest number that can be formed by 'turning on' the specified
    amount of digits in a given number.
    """
    list_length = len(battery_list)

    if number_length == 0:
        return result

    digit = max(battery_list[:list_length - number_length + 1])
    digit_i = battery_list.index(digit)
    result.append(digit)

    return find_number(battery_list[digit_i + 1:], number_length - 1, result)


total_output_joltage = 0


for bank in power_banks:
    joltages = list(map(int, list(bank.strip())))
    length = len(joltages)

    total_output_joltage_list = find_number(joltages, 12, [])
    joltage_int = int("".join(map(str, total_output_joltage_list)))

    total_output_joltage += joltage_int


print(f"Output: {total_output_joltage}")
