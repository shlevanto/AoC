import re

spelled = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4", 
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
 }

with (open("1b.txt", "r")) as file:
    lines = file.readlines()

sum = 0

for line in lines:
    digits = []
    for c in range(0, len(line)):
        if str.isdigit(line[c]):
            digits.append(line[c])
        else:
            for i in range(1, 6):
                substring = line[c:c+i]
                if substring in spelled.keys():
                    digits.append(spelled[substring])
    calib = digits[0] + digits[-1]
    sum += int(calib)
print(sum)
                                 
"""
sum = 0

for item in lines:
        digits = list(filter(str.isdigit, item))
        calib = digits[0] + digits[-1]
        sum += int(calib)

print(sum)
"""