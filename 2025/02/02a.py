import sys
from functools import reduce
import re

in_file = sys.argv[1]

with open(in_file, "r") as f:
    input_string = f.read()

ranges = input_string.split(",")

# find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. 
# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice)

sum_of_ids = 0
# should be     1227775554
# is            3349775553
for r in ranges:

    begin = r.split("-")[0]
    end = r.split("-")[1]

    for s in range(int(begin), int(end) + 1):
        id = str(s)
        half = len(id) // 2

        head = id[:half]
        tail = id[half:]

        if head == tail:
            sum_of_ids += s
            #print(id)

print(f"result: {sum_of_ids}")