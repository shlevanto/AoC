import itertools

file_path = "07.input"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

inputs = {
    int(line.split(":")[0].strip()): 
        [int(x) for x in line.split(":")[1].strip().split(" ")] 
        for line in lines
        }


def calculate(op_arr, arr, max_value):
    res = arr.pop(0)
    while len(op_arr) > 0:
        a = arr.pop(0)
        op = op_arr.pop(0)
        if op == "+":
            res += a
        if op == "*":
            res *= a
        if res > max_value:
            return False

    return res == max_value


def check_calibration(end_result, equation):
    operators = ["+", "*"]
    op_arr = list(itertools.product(operators, repeat=len(equation)-1))

    for ops in op_arr:
        if calculate(list(ops), equation.copy(), end_result):
            return end_result
    return 0

print(sum(check_calibration(item, inputs[item]) for item in inputs))
