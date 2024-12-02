with open("01.input") as file:
    lines = [line.strip() for line in file]

first = []
second = []

for line in lines:
    split_line = line.split("  ")
    first.append(split_line[0].strip())
    second.append(split_line[1].strip())

second_dict = {}

for a in second:
    if a in second_dict.keys():
        second_dict[a] += 1
    else:
        second_dict[a] = 1

similarities = 0

for b in first:
    # go through list and get occurences from second
    if b in second_dict.keys():
        similarities += int(b) * second_dict[b]

print(similarities)