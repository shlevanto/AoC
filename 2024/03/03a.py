import re


with open("03.txt") as file:
    s = file.read()

pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")
matches = re.findall(pattern, s)

def multiply(s):
    mul_pattern = re.compile(r"[0-9]+")
    factors = re.findall(mul_pattern, s)
    return int(factors[0]) * int(factors[1])

result = sum([multiply(factors) for factors in matches])

print(result)