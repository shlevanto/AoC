from enum import Enum

class Hand(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

card_values_1 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10
}

card_values_2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10
}

def get_card_value(card, jokers):
    if jokers:
        values = card_values_2
    else:
        values = card_values_1  
    
    if card.isdigit():
        return int(card)
    else:
        return values[card]
    
filename = "input.txt"

with open(filename, "r") as file:
    lines = file.readlines()


hands = [(line.split()[0], line.split()[1]) for line in lines]


def check_hand(hand, jokers):
    checkable = set(hand)
    
    match len(checkable):
        case 1:
            return Hand.FIVE_OF_A_KIND
        case 2:
            for card in checkable:
                if jokers and hand.count("J") > 0:
                    return Hand.FIVE_OF_A_KIND
                if hand.count(card) == 4:
                    return Hand.FOUR_OF_A_KIND
            return Hand.FULL_HOUSE
        case 3:
            if jokers and hand.count("J") == 3:
                return Hand.FOUR_OF_A_KIND
            if jokers and hand.count("J") == 2:
                return Hand.FOUR_OF_A_KIND
                        
            for card in checkable:
                if hand.count(card) == 3:
                    if jokers and hand.count("J") == 1:
                        return Hand.FOUR_OF_A_KIND
                    return Hand.THREE_OF_A_KIND
                if hand.count(card) == 2:
                    if jokers and hand.count("J") == 1:
                        return Hand.FULL_HOUSE
            return Hand.TWO_PAIR 
        case 4:
            if jokers and hand.count("J") > 0:
                return Hand.THREE_OF_A_KIND
            return Hand.ONE_PAIR
        case 5:
            if jokers and hand.count("J") > 0:
                return Hand.ONE_PAIR
            return Hand.HIGH_CARD
        case _:
            return None
        

def do_result(the_hands, jokers):
    hand_rankings = [
        (
            hand[0], hand[1], 
            get_card_value(hand[0][0], jokers), 
            get_card_value(hand[0][1], jokers), 
            get_card_value(hand[0][2], jokers), 
            get_card_value(hand[0][3], jokers), 
            get_card_value(hand[0][4], jokers), 
            check_hand(hand[0], jokers)
            ) 
            for hand in the_hands
        ]

    ranked_hands = sorted(hand_rankings, key = lambda x: (x[7].value, x[2], x[3], x[4], x[5], x[6]))

    sum = 0

    for count, hand in enumerate(ranked_hands):
        sum += (count + 1) * int(hand[1])

    return sum

print(f"Task1: {do_result(hands, jokers=False)}")
print(f"Task2: {do_result(hands, jokers=True)}")
