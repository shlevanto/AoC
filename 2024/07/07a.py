import itertools

file_path = "07.input"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()


def calculate(op_arr, arr, max_value):
    res = arr[0]
    i = 1

    while len(op_arr) > 0:
        a = arr[i]
        op = op_arr.pop(0)
        if op == "+":
            res += a
        if op == "*":
            res *= a
        if res > max_value:
            return False
        i += 1

    return res == max_value


def check_calibration(line):
    end_result_string, equation_string = line.split(":")

    equation = [int(x) for x in equation_string.strip().split(" ")]
    end_result = int(end_result_string)

    operators = ["+", "*"]
    op_arr = list(itertools.product(operators, repeat=len(equation)-1))

    for ops in op_arr:
        if calculate(list(ops), equation, end_result):
            return end_result
    return 0

print(sum(check_calibration(line) for line in lines))
