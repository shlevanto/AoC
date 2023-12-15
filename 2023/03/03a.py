import numpy as np

array = np.loadtxt("input.txt", dtype="str", comments=None)


# 1. record the location for all symbols

symbols = set([])

for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        if array[i][j].isdigit() or array[i][j] == ".":
            continue
        else:
            symbols.add((i,j))


# 2. record location for all numbers

numbers = []

for i in range(0, len(array)):
    j = 0
    while j <  len(array[i]):
        number_length = 0
        if array[i][j].isdigit():
            number_start = j
            while array[i][j].isdigit():
                j += 1
                number_length += 1
                if(j >= len(array[i])):
                    break
            number = array[i][number_start:number_start + number_length]
            numbers.append((i, number_start, number_length, number))
        else:
            j += 1

# 3. check adjacenies and add to sum

machine_sum = 0

def check(number):
    # check row above
    row_above = number[0] - 1
    for i in range(number[1] - 1,  number[1] + number[2] + 1):
        if (row_above, i) in symbols:
            return int(number[3])

    # check row below
    row_below = number[0] + 1
    for i in range(number[1] - 1,  number[1] + number[2] + 1):
        if (row_below, i) in symbols:
            return int(number[3])

    # check ends
    if (number[0], number[1] - 1) in symbols:
        return int(number[3])

    if (number[0], number[1] + number[2]) in symbols:
        return int(number[3])

    else:
        return 0

for number in numbers:
    machine_sum += check(number)

print(machine_sum)
