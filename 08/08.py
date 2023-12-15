from itertools import cycle
from functools import reduce

filename = "input.txt"

with open(filename, "r") as file:
    lines = file.readlines()

instructions = lines[0].strip()

origin = "AAA"

navigation = {}

for line in lines[1:]:
    if len(line) > 1:
        key = line.split("=")[0].strip()  
        value = line.split("=")[1].replace("(", "").replace(")", "").strip().split(",")
        value = [v.strip() for v in value]
        navigation[key] = value


def find_route(location, instruction, navigation, ghost):
    pool = cycle(instructions)

    moves = 0
    
    for step in pool:

        match(step):
            case "L":
                location = navigation[location][0]
            case "R":
                location = navigation[location][1]
        moves += 1

        if not ghost and location == "ZZZ":
            return moves
        if ghost and location[2] == "Z":
            return moves
    
    return moves        

# task 1
print(find_route(origin, instructions, navigation, ghost=False))

# task 2

# get all start locations
ghost_origins = [x for x in navigation.keys() if x[2]=="A"]

ghost_trails = [find_route(ghost_origin, instructions, navigation, ghost=True) for ghost_origin in ghost_origins]

ghost_trails = [2,3,4,5,6,7,867]

def find_ghost_trail(trails):
    result = trails.copy()


    while len(set(result)) > 1:
        i = result.index(min(result))
        result[i] += trails[i]

    return set(result)


print(find_ghost_trail(ghost_trails))
