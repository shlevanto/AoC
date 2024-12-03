import re

test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("03.txt") as file:
    s = file.read()

pattern = re.compile(r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)")
matches = re.findall(pattern, s)

def multiply(s):
    mul_pattern = re.compile(r"[0-9]+")
    factors = re.findall(mul_pattern, s)
    return int(factors[0]) * int(factors[1])

result = 0
enabled = True

for a in matches:
    if a == "do()":
        enabled = True
        continue

    if a == "don't()":
        enabled = False
        continue

    if enabled:
        result += multiply(a)


print(result)