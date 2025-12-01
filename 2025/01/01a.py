with open("input.txt", "r") as f:
    codes = f.readlines()

password = 0
position = 50

for code in codes:

    # rotate

    # check if passes zero and update position

    # add complete rounds
    direction = code[0]
    steps = int(code[1:].strip()) % 100

    if direction == "L":
        position = position - steps
    if direction == "R":
        position = position + steps 

    if position < 0:
        position = 100 + position

    if position >= 100:
        position = position - 100

    if position == 0:
        password += 1

print(password)