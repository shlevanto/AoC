with open("02.txt", "r") as file:
    lines = file.readlines() 

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

valid_games_sum = 0

for line in lines:
    game_id = int(line.split(":")[0].replace("Game ", ""))
    samples = line.split(":")[1:][0].split(";")

    valid_game = True
    
    for sample in samples:
        sample_split = sample.split(",")

        for item in sample_split:
            case = item.strip().split(" ")
            if int(case[0]) > maxes[case[1]]:
                valid_game = False
    
    if valid_game:
        valid_games_sum += game_id

print(valid_games_sum)
