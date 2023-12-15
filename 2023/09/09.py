import sys
from functools import reduce
import operator

filename = str(sys.argv[1])

with open(filename, "r") as f:
    lines = f.readlines()

sequences = [[int(x) for x in line.split()] for line in lines]


def iterate(count, iterations, sequence):
    if reduce(operator.add, iterations[-1]) == 0:
        return iterations

    iteration = []

    for count, value in enumerate(sequence):
        if count == len(sequence) - 1:
            break
        iteration.append(sequence[count + 1] - value)

    iterations.append(iteration)

    return iterate(count + 1, iterations, iteration)

# Task 1, next value
result_1 = 0

for seq in sequences:
    iterated = iterate(count=0, iterations=[seq], sequence=seq)
    next_value = 0

    for i in iterated:
        next_value += i[-1]

    result_1 += next_value

print(result_1)

# Task 2, previous value
result_2 = 0

for seq in sequences:
    iterated = list(reversed(iterate(count=0, iterations=[seq], sequence=seq)))
    next_value = 0
    for count, i in enumerate(iterated):
        if count == len(iterated) - 1:
            break

        next_value = iterated[count + 1][0] - next_value

    result_2 += next_value


print(result_2)
