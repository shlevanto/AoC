import numpy as np
import re

file_name = "04.input"

with open(file_name, "r") as f:
    rows = f.readlines()

chars = [list(row.strip()) for row in rows]

arr = np.stack(chars)
columns = ["".join(arr[:, i]) for i in range(0, arr.shape[0])]
diagonals = ["".join(arr.diagonal(offset = i)) for i in range(-(arr.shape[0] - 1), arr.shape[0])]


def counter(item):
    pattern = re.compile(r"(?=(XMAS|SAMX))")
    matches = re.finditer(pattern, item)
    no_matches = len([match.group(1) for match in matches])
    return no_matches

all_input = rows + columns + diagonals

print([counter(item) for item in diagonals])
