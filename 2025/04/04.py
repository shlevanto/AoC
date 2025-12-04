import sys
from asyncio import SelectorEventLoop

import numpy as np


def outside_map(storage_map, r, c):
    """Is the neighbouring tile to be checked outside the map."""
    res = r < 0 or c < 0 or r >= storage_map.shape[0] or c >= storage_map.shape[1]
    return res


def access_clear(storage_map, r, c):
    """Can this location be accessed."""
    blocks = 0
    directions = [
        (-1, -1),  # up left
        (-1, 0),  # up
        (-1, 1),  # up right
        (0, -1),  # left
        (0, 1),  # right
        (1, -1),  # down left
        (1, 0),  # down
        (1, 1),  # down right
    ]

    for d in directions:
        out_of_bounds = outside_map(storage_map, r + d[0], c + d[1])
        if out_of_bounds:
            continue
        if storage_map[r + d[0], c + d[1]]:
            blocks += 1
        if blocks >= 4:
            return False
    return True


def solution_1(storage_map):
    """Find all accessible locations."""
    rows = storage_map.shape[0]
    columns = storage_map.shape[1]

    # traverse
    accessible = 0

    for r in range(0, rows):
        for c in range(0, columns):
            if not storage_map[r, c]:
                continue
            if access_clear(storage_map, r, c):
                accessible += 1

    return accessible


def solution_2(storage_map, cleared_map):
    """Find all accesible locations, clear them and reiterate with the cleared storage map."""

    rows = storage_map.shape[0]
    columns = storage_map.shape[1]
    # traverse
    accessible = 0

    for r in range(0, rows):
        for c in range(0, columns):
            if not storage_map[r, c]:
                continue
            if access_clear(storage_map, r, c):
                accessible += 1
                cleared_map[r, c] = False
    if accessible == 0:
        return np.sum(cleared_map)

    return solution_2(cleared_map, np.copy(cleared_map))


def main():
    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        input_string = f.readlines()

    input_string = [s.strip() for s in input_string]

    columns = len(input_string[0])
    rows = len(input_string)

    # parse to 2d array
    storage_map = np.zeros((rows, columns), np.bool)

    for i, s in enumerate(input_string):
        for j, item in enumerate(s):
            storage_map[i, j] = item == "@"

    result_1 = solution_1(storage_map)
    # Solution 2 returns the amount of locations that can not be cleared.
    result_2 = np.sum(storage_map) - solution_2(storage_map, np.copy(storage_map))

    print(f"Part one: {result_1}")
    print(f"Part two: {result_2}")


if __name__ == "__main__":
    main()
