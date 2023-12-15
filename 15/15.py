import sys
import re
from collections import OrderedDict

filename = sys.argv[1]

with open(filename, "r") as f:
    data = f.read()

data = data.split(",")

sum = 0

# part 1: calculate HASH
def calculate_HASH(code):
    hash_value = 0
    
    for char in code:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    
    return hash_value

sum = 0

for code in data:
    sum += calculate_HASH(code)

print(sum)

# part 2: HASHMAP
boxes = OrderedDict()

pattern = r'[-=]'
for code in data:
    
    split_code = re.split(pattern, code) 
    
    label = split_code[0]
    focus = split_code[1]

    match focus:
        case "":
            try:
                boxes.pop(label, None)
            except KeyError:
                pass
        case _:
            boxes[label] = focus

print(boxes)


