import numpy as np
import re

file_name = "04_long.input"

with open(file_name, "r") as f:
    rows = f.readlines()

# create an array of characters
chars = [list(row.strip()) for row in rows]
arr = np.stack(chars)

# create strings of columns and both directions of diagonals
columns = ["".join(arr[:, i]) for i in range(0, arr.shape[0])]
diagonals = ["".join(arr.diagonal(offset = i)) for i in range(-(arr.shape[0]), arr.shape[0])]
diagonals_2 =  ["".join(np.flip(arr, axis=1).diagonal(offset = i)) for i in range(-(arr.shape[0]), arr.shape[0])]


def counter(item):
    #this pattern allows for overlapping
    pattern = re.compile(r"(?=(XMAS|SAMX))")
    matches = re.finditer(pattern, item)
    no_matches = len([match.group(1) for match in matches])
    
    return no_matches

# combine all inputs
all_input = rows + columns + diagonals + diagonals_2

print(sum([counter(d) for d in all_input]))
