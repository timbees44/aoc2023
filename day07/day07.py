"""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def part_one(input):
    with open(input, "r") as f:
        hand = [x.split() for x in f]
        for card in hand[0]:
            cards = {"A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0}
            for k, v in cards.items():
                if k == card:
                    cards[k] += 1



if __name__ == "__main__":
    part_one("test.txt")
