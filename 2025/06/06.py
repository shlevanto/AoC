import operator
import sys
from functools import reduce

import numpy as np

OPS = {"+": operator.add, "*": operator.mul}


def parse_input_1(file_name):
    with open(file_name, "r") as f:
        input_string = [line.strip() for line in f.readlines()]

    math_homework = list()
    operators = list()

    for line in input_string:
        try:
            math_homework.append([int(a) for a in line.split()])
        except Exception as e:
            operators = line.split()

    return np.stack(math_homework), operators


def parse_input_2(file_name):
    with open(file_name, "r") as f:
        input_string = [line[:-1] for line in f.readlines()]

    math_homework = list()
    operators = input_string[-1]

    # for some reason text files will strip trailing whitespaces from the last line...
    # this fixes it:
    padding = len(input_string[0]) - len(operators)
    operators += " " * padding

    # operators are spaced unevenly, but they mark the beginning of each column of numbers
    operator_locations = [i for i, o in enumerate(operators) if o != " "]

    for line in input_string[:-1]:
        # split line into slices according to operator locations
        split_line = list()
        for i in range(len(operator_locations)):
            start = operator_locations[i]
            try:
                end = operator_locations[i + 1]
            except:
                end = len(line) + 1

            list_slice = line[start : end - 1]
            split_line.append(list_slice)
        math_homework.append(split_line)

    return np.stack(math_homework), operators.split()


def solution_1(math_homework, operators):
    grand_total = 0

    for i in range(math_homework.shape[1]):
        operator = OPS[operators[i]]
        grand_total += reduce(operator, math_homework[:, i])

    return grand_total


def solution_2(math_homework, operators):
    grand_total = 0

    for i in range(math_homework.shape[1]):
        operator = OPS[operators[i]]

        human_numbers = math_homework[:, i]
        cephalopod_numbers = list()

        for i in range(len(human_numbers[0])):
            cephalopod_number = ""
            for number in human_numbers:
                cephalopod_number += number[i]
            cephalopod_numbers.append(int(cephalopod_number.strip()))

        grand_total += reduce(operator, cephalopod_numbers)

    return grand_total


def main():
    file_name = sys.argv[1]

    math_homework_1, operators_1 = parse_input_1(file_name)
    math_homework_2, operators_2 = parse_input_2(file_name)
    result_1 = solution_1(math_homework_1, operators_1)
    result_2 = solution_2(math_homework_2, operators_2)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")


if __name__ == "__main__":
    main()
