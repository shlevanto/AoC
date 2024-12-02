

with open("02.input") as file:
    lines = file.readlines()

int_lines = []

for line in lines:
    int_line = [int(number) for number in line.split(" ")]
    int_lines.append(int_line)

def check_order(list):
    return list == sorted(list) or list == sorted(list, reverse=True)

def check_differences(list):
    for i in range(len(list) - 1):
        val = abs(list[i] - list[i+1])
        if val < 1 or val > 3:
            return False
    return True

def check_safety(list):
    if check_order(list):
        return check_differences(list)
    return False

print(sum([check_safety(line) for line in int_lines]))

