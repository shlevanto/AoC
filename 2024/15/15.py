import numpy as np 


def prepare_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    map_raw = []
    instructions_raw = []

    target = map_raw

    for line in lines:
        if line == "\n":
            target = instructions_raw
        target.append(line.strip())

    chars = [[x for x in list(row.strip())] for row in map_raw]
    map = np.stack(chars)
    
    instructions = "".join(instructions_raw)

    return map, instructions


def is_wall(arr, location):
    return arr[location] == "#"


def is_box(arr, location):
    return arr[location] == "O"


def step(obj, direction):
    y, x = obj
    match direction:
        case "^":
            return y - 1, x
        case "v": 
            return y + 1, x
        case ">":
            return y, x + 1
        case "<":
            return y, x - 1


def move(obj, type, map, directions):  
    for d in directions:
        if type == "@":
            print(d)
        next_location = step(obj, d)
       
        if is_wall(map, next_location):
            print(map, "\n****\n")
            if type == "O":
                return True
            else:
                continue
        
        if is_box(map, next_location):
            wall = move(next_location, "O", map, [d])
            if wall:
                continue
            map[obj] = "."
            obj = next_location
            map[next_location] = type
            
            
        map[obj] = "."
        obj = next_location
        map[next_location] = type
        
        print(map, "\n****\n")
    
    return True
        

    

def find_robot(arr):
    location = (-1, -1)
    
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            if arr[y][x] == "@":
                location = (y, x)
    
    return location 


if __name__ == "__main__":
    file_path = "15_tiny.input"
    map, instructions = prepare_input(file_path)

    robot = find_robot(map)
    
    move(robot, "@", map, instructions)

    

   

    
