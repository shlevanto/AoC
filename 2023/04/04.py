from functools import reduce
import operator

filename = "input.txt"

with open(filename, "r") as file:
    lines = file.readlines()

sum = 0

extra_cards = []

for count, line in enumerate(lines):
    line = line.strip().split(":")
    line = line[1].split("|")

    my_numbers = [int(n) for n in line[0].split(" ") if n.isdigit()]
    winning_numbers = [int(n) for n in line[1].split(" ") if n.isdigit()]

    wins = -1
    more_cards = 0

    for number in my_numbers:
        if number in winning_numbers:
            wins += 1
            more_cards += 1

    if wins >= 0:
        sum += 2**wins
        extra_cards.append(more_cards)
    else:
        extra_cards.append(0)

final_no_cards = [1] * len(lines)

for count, value in enumerate(extra_cards):
    for i in range(1, value + 1):
        final_no_cards[count + i] += final_no_cards[count]

print("Task 1: ", sum)
print("Task 2: ", reduce(operator.add, final_no_cards))
