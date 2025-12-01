from functools import reduce
from operator import mul
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

# dimensions y, x
arr = (103,101)

file_path = "14.input"

with open(file_path, "r") as f:
    input_string = f.readlines()

a = [s.strip().split("=") for s in input_string]

robots = []

for s in a:
    position_list = s[1].split("v")[0].split(",")
    position = (int(position_list[0]), int(position_list[1]))

    velocity = (int(s[2].split(",")[0]), int(s[2].split(",")[1])) 
    
    robot = {"p": position, "v": velocity}
    robots.append(robot)


def move(robot, steps, dimensions):
    v_x, v_y = robot["v"]
    p_x, p_y = robot["p"]
    y, x = dimensions

    end_x = (p_x + steps * v_x) % x
    end_y = (p_y + steps * v_y) % y

    return (end_x, end_y)

def quadrant_counts(arr, end_positions):
    a, b, c, d = 0, 0, 0, 0
    mid_y, mid_x = arr[0] // 2, arr[1] // 2

    for robot in end_positions:
        if robot[0] == mid_x or robot[1] == mid_y:
            continue
        if robot [0] < mid_x and robot[1] < mid_y:
            a += 1
        if robot [0] > mid_x and robot[1] < mid_y:
            b += 1 
        if robot [0] < mid_x and robot[1] > mid_y:
            c += 1
        if robot [0] > mid_x and robot[1] > mid_y:
            d += 1   
    
    return (a, b, c, d)

def draw_positions(positions, arr):
    canvas = np.zeros()

seconds = 100
iterations = 5000

end_positions = [move(robot, seconds, arr) for robot in robots]
quadrants = quadrant_counts(arr, end_positions)

print("Puzzle 1:", reduce(mul, quadrants))

# looking for christmas trees...
for i in range(iterations):
    print("seconds:", i+1)
    for robot in robots:
        robot["p"] = move(robot, 1, arr)
    
    positions = [robot["p"] for robot in robots]
    
    canvas = np.zeros(arr, dtype=str)

    for p in positions:
        canvas[p[1], p[0]] = "*"

    for row in range(arr[0]):
        print(canvas[row,:].tolist())

    print("*****\n\n\n")
    

    


