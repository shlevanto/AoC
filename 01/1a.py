with (open("1a.txt", "r")) as file:
    lines = file.readlines()

print(lines)

sum = 0

for item in lines:
        digits = list(filter(str.isdigit, item))
        calib = digits[0] + digits[-1]
        sum += int(calib)
print(sum)
