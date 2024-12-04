import numpy as np
import re

file_name = "04_long.input"

with open(file_name, "r") as f:
    rows = f.readlines()

# create an array of characters
chars = [list(row.strip()) for row in rows]
arr = np.stack(chars)
flip_arr = np.flip(arr, axis=1)

# create strings of columns and both directions of diagonals
columns = ["".join(arr[:, i]) for i in range(0, arr.shape[0])]
diagonals = ["".join(arr.diagonal(offset = i)) for i in range(-(arr.shape[0]), arr.shape[0])]
diagonals_2 =  ["".join(flip_arr.diagonal(offset = i)) for i in range(-(arr.shape[0]), arr.shape[0])]


def counter(item):
    #this pattern allows for overlapping
    pattern = re.compile(r"(?=(XMAS|SAMX))")
    matches = re.finditer(pattern, item)
    no_matches = len([match.group(1) for match in matches])

    return no_matches

# combine all inputs
all_input = rows + columns + diagonals + diagonals_2

print("Puzzle 1:", sum([counter(d) for d in all_input]))

# Puzzle two: find each A and check if it is the center of an X-MAS
# Ignore all As on first and last row and column

def check_cross(i, j, arr):
    ul = arr[i-1, j+1]
    ur = arr[i+1, j+1]
    dl = arr[i-1, j-1]
    dr = arr[i+1, j-1]

    word_1 = ul + arr[i,j] + dr
    word_2 = ur + arr[i,j] + dl

    words = [word_1, word_2]
    if words.count("SAM") + words.count("MAS") == 2:
        return True
    return False

count = 0

for i in range(1, arr.shape[0] - 1):
    for j in range(1, arr.shape[1] - 1):
        if arr[i,j] == "A" and check_cross(i, j, arr):
            count += 1

print("Puzzle 2:", count)
