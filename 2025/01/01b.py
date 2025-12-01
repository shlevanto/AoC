with open("input.txt", "r") as f:
    codes = f.readlines()

password = 0
position = 50

# between 6165 and 6707

for code in codes:

    direction = code[0]
    number = int(code[1:].strip())
    complete = number // 100
    steps = number % 100

    if direction == "L":
        position = position - steps
    if direction == "R":
        position = position + steps 

    if position <= 0:
        password += 1
        position = 100 + position

    if position > 100:
        password += 1
        position = position - 100

    #password += complete

print(password)