filename = "example.txt"

with open(filename, "r") as file:
    lines = file.readlines()

class Map:
    def __init__(self, destination_start, source_start, length):
        self.source_start = source_start
        self.length = length
        self.source_end = self.source_start + self.length - 1
        self.destination_start = destination_start

    def __str__(self):
        return f"***\nSource start: {self.source_start}\nSource end: {self.source_end}\nDestination start: {self.destination_start}\nLength: {self.length}\n***"

    def convert(self, value):
        return value - self.source_start + self.destination_start


def collect_values(line):
    return [int(x) for x in line.split(" ")]

def create_map(line):
    values = collect_values(line)
    the_map = Map(values[0], values[1], values[2])
    return the_map

seeds = collect_values(lines[0].split(":")[1].strip())

mappings = {
    "seed-to-soil map": [],
    "soil-to-fertilizer map": [],
    "fertilizer-to-water map": [],
    "water-to-light map": [],
    "light-to-temperature map": [],
    "temperature-to-humidity map": [],
    "humidity-to-location map": [],
}
for count, line in enumerate(lines[1:]):
    title = line.split(":")[0].strip()
    if title in mappings:
        count += 2
        while lines[count][0].isdigit():
            mappings[title].append(create_map(lines[count].strip()))
            if count == len(lines[1:]):
                break    
            count += 1



locations_1 = []

for seed in seeds:
    for category in mappings:
        maps = mappings[category]
        for map in maps:
            if seed >= map.source_start and seed <= map.source_end:
                seed = map.convert(seed)
                break
    locations_1.append(seed)

result_1 = min(locations_1)
print(result_1)

seed_ranges = []

while seeds:
    range_start = seeds.pop(0)
    length = seeds.pop(0)
    seed_ranges.append((range_start, range_start + length))


print(seed_ranges)