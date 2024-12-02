with open("02.input") as file:
    lines = file.readlines()

int_lines = []

for line in lines:
    int_line = [int(number) for number in line.split(" ")]
    int_lines.append(int_line)

# create o
def permutate(list):
    reversed = list[::-1]
    permutations = [list, revesed]

    for i in range(0, len(list)):
        permutations.append(list[:i] + list[i+1:])
        permutations.append(reversed[:i] + reversed[i+1:])
    
    return permutations


def check_order(list):
    return list == sorted(list) 

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

def check_permutations(list):
    permutations = permutate(list)
    
    for p in permutations:
        if check_safety(p):
            return True
    
    return False

print(sum([check_permutations(list) for list in int_lines]))