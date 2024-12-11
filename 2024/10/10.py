import numpy as np

global counter
counter = 0

# 1. read input 
# 2. graph representation?
# 3. look for trailheads 0
# 4. iterate through input, do a bfs at each trailhead 
file_path = "10.input"
with open(file_path, "r") as f:
    rows = f.readlines()

# create an array of characters
chars = [[int(x) for x in list(row.strip())] for row in rows]
arr = np.stack(chars)


def is_allowed(node, arr):
    y, x = node

    # top or bottom wall
    if y == -1 or y >= arr.shape[0]:
        return False
    # side wall
    if x == -1 or x >= arr.shape[1]:
        return False

    return True

def is_adjacent(arr, node, next):
    
    if is_allowed(next, arr):
        return arr[next] == arr[node] + 1
    return False


def trail(start, arr, value, visited):
    if not is_allowed(start, arr) or visited[start]:
        return
    visited[start] = True
    value = arr[start]

    if value == 9:
        global counter
        counter += 1

    y, x = start
    neighbours = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]

    for n in neighbours: 
        if is_adjacent(arr, start, n):
            trail(n, arr, value, visited) 



for y in range(arr.shape[0]):
    for x in range(arr.shape[1]):
        if arr[y,x] == 0:
            visited = np.zeros_like(arr, dtype=bool)
            trail((y,x), arr, 0, visited)

print("Puzzle 1, trail scores:", counter)