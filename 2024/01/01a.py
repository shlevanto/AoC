with open("01.input") as file:
    lines = [line.strip() for line in file]

first = []
second = []

for line in lines:
    split_line = line.split("  ")
    first.append(split_line[0].strip())
    second.append(split_line[1].strip())

first.sort()
second.sort()

sum_of_distances = 0

for a, b in zip(first,second):
    sum_of_distances += abs((int(a)-int(b)))

print(sum_of_distances)