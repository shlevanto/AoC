from functools import reduce
import operator

with open("02.txt", "r") as file:
    lines = file.readlines() 



power_sum = 0

for line in lines:
    game_id = int(line.split(":")[0].replace("Game ", ""))
    samples = line.split(":")[1:][0].split(";")

    maxes = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    
    for sample in samples:
        sample_split = sample.split(",")

        for item in sample_split:
            case = item.strip().split(" ")
            if int(case[0]) > maxes[case[1]]:
                maxes[case[1]] = int(case[0])
    power_sum += reduce(operator.mul, list(maxes.values()))
    
print(power_sum)
