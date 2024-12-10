file_path = "09_short.input"

with open(file_path, "r") as f:
    input_string = f.read()

# 1. Create empty list
disk_map = []
# 2. Parse alternatingly from beginning and end of input

j = 0

for i, e in enumerate(input_string):
    if i % 2 == 0:
        print(input_string[i])
        for i in range(int(input_string[i])):
            disk_map.append(int(input_string[i]))
    else: 
        end = -1 - j
        print(input_string[end])
        j += 1

# 3. From end concatenate digits and place them into the array
# ie. 12343 = 0..111....222 = 0221112 = [0, 22, 1, 1, 1, 2]
# 4. Use an iterator to calculate checksum, split numbers into digits if number > 9

print(disk_map)