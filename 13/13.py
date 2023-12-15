import sys
import numpy as np

filename = str(sys.argv[1])

with open(filename) as f:
    lines = f.readlines()

lines = [list(line.strip()) for line in lines]

paths = np.array(lines, ndmin=2)

# find reflected columns

def mirror_location(paths, axis):
    match axis:
        case 0:
            data = paths        
        case 1:
            data = paths.T
        case _:
            raise ValueError("axis must be 0 or 1") 

    for count, part in enumerate(data):
        print(count, part)
        try:
            if np.array_equal(data[count], data[count+1]):            
                return (count, count+1)
        except:
            continue
    return None


def reflection_depth(loc, paths, axis):
    depth = 0
    left, right = loc

    match axis:
        case 0:
            data = paths        
        case 1:
            data = paths.T
        case _:
            raise ValueError("axis must be 0 or 1") 

    while True:
        try:
            if np.array_equal(paths[left-depth], paths[right+depth]):
                depth += 1
            else:
                break
        except:
            break
    
    return depth


loc_cols = mirror_location(paths, axis=1)
loc_rows = mirror_location(paths, axis=0)

cols = reflection_depth(loc_cols, paths, axis=1)
rows = reflection_depth(loc_rows, paths, axis=0)    

print(cols, rows)
reflection = max(cols, rows)

print(reflection)




