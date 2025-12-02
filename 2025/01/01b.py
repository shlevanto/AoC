# This does not work :(

with open("input.txt", "r") as f:
    codes = f.readlines()

password = 0
position = 50

# between 6165 and 6707
for i, code in enumerate(codes):

    #print(f"{i}: rotating {code.strip()}")

    direction = code[0]
    number = int(code[1:].strip())

    if direction == "L":
        if position == 0:
            position = 100
        position -= number

    if direction == "R":
        if position == 100:
            position = 0
        position += number

    rounds = abs(position) // 100

    if position < 0:
        password += 1
        position = abs(position % 100)
        password += rounds

    if position > 100:
        position = position % 100
        password += rounds

    if position % 100 == 0:
        password += 1


    #print(f"landed on {position}, password is {password}\n")

print(f"The password is: {password}")