import sys
from functools import reduce
import re

in_file = sys.argv[1]

with open(in_file, "r") as f:
    input_string = f.read()

ranges = input_string.split(",")

# find the invalid IDs by looking for any ID which is 
# made only of some sequence of digits repeated twice or more. 
# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice)



def match_patterns(id_string):
    # quick check if all numbers in id are the same
    if len(id_string) == 1:
        return 0

    if len(set(id_string)) == 1:
        #print(f"id: {id_string}, match: {id_string}")
        return int(id_string)

    for i in range(2, len(id_string) // 2 + 1):
        pattern = id[:i]
        #print(pattern, re.findall(pattern, id_string))
        res = "".join(re.findall(pattern, id_string))
        if res == id:
            #print(f"id: {id_string}, match: {res}")
            return int(id_string)

    return 0


sum_of_ids = 0

for r in ranges:

    begin = r.split("-")[0]
    end = r.split("-")[1]

    for s in range(int(begin), int(end) + 1):
        id = str(s)
        sum_of_ids += match_patterns(id)

print(f"result: {sum_of_ids}")