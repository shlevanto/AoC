import math

file_path = "05.input"

with open(file_path,'r') as f:
    lines = f.read().splitlines()


# find element to split at
def find_split(array, marker):
    for i, item in enumerate(array):
        if item == marker:
            return i
    return -1


def split_array(array, marker):
    split = find_split(array, marker)
    return (array[:split], array[split+1:])

instructions, raw_pages = split_array(lines, "")

manuals = [manual.split(",") for manual in raw_pages]

# combine rules for each first mentioned page number

instruction_dic = {}

for item in instructions:
    first, second = item.split("|")
    if first in instruction_dic:
        instruction_dic[first].append(second)
    else:
        instruction_dic[first] = [second]



def validate(manual):
# for each list check if instructions are relevant
# if not, approve list

    valid = True

    for key, value in instruction_dic:
        if key in manual and value in manual:
            valid = True
            break

    # if yes, check order and break if list is disapproved

    if valid:
        order = dict((j,i) for i, j in enumerate(manual))
        for page in manual:
            for i in instruction_dic:
                for value in instruction_dic[i]:
                    if value not in order or i not in order:
                        continue
                    elif order[i] > order[value]:
                        valid = False

    return valid  

def middle(manual):
    return int(manual[math.floor(len(manual) / 2)])

print(sum(middle(manual) for manual in manuals if validate(manual)))








