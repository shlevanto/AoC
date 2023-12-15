import sys
import numpy as np

filename = str(sys.argv[1])

with open(filename) as f:
    lines = f.readlines()

lines = [list(line.strip()) for line in lines]

# Convert star nodes to numbers

numbering = 0

for count, line in enumerate(lines):
    for count_c, c in enumerate(line):
        if c == "#":
            lines[count][count_c] = numbering
            numbering += 1

class Node:
    def __init__(self, origin, destination, weight):
        self.origin = origin
        self.destination = destination
        self.weight = weight
    
    def _str__(self):
        return f"({origin}, {destination}, w: {weight})"

# Convert to numpy array
starmap = np.array(lines, ndmin=2)

# find empty rows and columns
empty_rows = [row_no for row_no, row in enumerate(starmap) if np.all(row == ".")]
empty_cols = [col_no for col_no, col in enumerate(starmap.T) if np.all(col == ".")]

# read map to adjacency matrix
no_nodes = len(lines) * len(lines[0])
graph = np.zeros((no_nodes, no_nodes), dtype=int)

def up(row, col, emptycol):
    try:
        neighbour = starmap[row-1][col]
        if row-1 in empty_rows and not emptycol:
            return 2
        else:
            return 1
    except:
        return None
    
def down(row, col, emptycol):
    try:
        neighbour = starmap[row+1][col]
        if row+1 in empty_rows and not emptycol:
            return 2
        else:
            return 1
    except:
        return None
    
def left(row, col, emptyrow):
    try:
        neighbour = starmap[row][col-1]
        if col-1 in empty_cols and not emptyrow:
            return 2
        else:
            return 1
    except:
        return None
    
def right(row, col, emptyrow):
    try:
        neighbour = starmap[row][col+1]
        if col+1 in empty_cols and not emptyrow:
            return 2
        else:
            return 1
    except:
        return None

def neighbours(row, col, emptyrow, emptycol):
    return [up(row, col, emptycol), down(row, col, emptycol), left(row, col, emptyrow), right(row, col, emptyrow)]

edges = []

for row_no, row in enumerate(starmap):
    emptyrow = row_no in empty_rows
    
    for col_no, col in enumerate(starmap.T):
        emptycol = col_no in empty_cols
        new_edges = neighbours(row_no, col_no, emptyrow, emptycol)
        [edges.append(n) for n in new_edges if n is not None]

print(edges)
# Floyd-Warshall, all shortest routes but only between numbered nodes
