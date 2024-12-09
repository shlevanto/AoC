import numpy as np

def to_numpy(file_path):
    with open(file_path, "r") as f:
        rows = f.readlines()

    # create an array of characters
    chars = [list(row.strip()) for row in rows]
    arr = np.stack(chars)

    return arr


def to_lines(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    return lines
