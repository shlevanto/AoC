from functools import reduce
import operator

filename = "input.txt"

with open(filename, "r") as f:
    lines = f.readlines()

times = [int(x) for x in lines[0].split(":")[1].strip().split()]
goals = [int(x) for x in lines[1].split(":")[1].strip().split()]

winning_times = []

def check_winning_times(time, goal, long=False):
    time_options = list(range(0, time + 1))
    charge = list(reversed(time_options))

    for count, time in enumerate(time_options):
        if time * charge[count] > goal:
            if long:
                return len(time_options) - 2 * count
            else:
                winning_times.append(len(time_options) - 2 * count)
                return

# Part 1
for time, goal in zip(times, goals):
    check_winning_times(time, goal)

print(reduce(operator.mul, winning_times))

# Part 2
long_time = int("".join(lines[0].split(":")[1].strip().split()))
long_goal = int("".join(lines[1].split(":")[1].strip().split()))

print(check_winning_times(long_time, long_goal, long=True))
