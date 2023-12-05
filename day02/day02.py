"""
test input:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

contraints:
12 red cubes, 13 green cubes, and 14 blue cubes
"""

import re

def part_one(input):
    with open(input, "r") as f:
        imposs = 0
        poss = 0
        game_total = 0
        for line in f:
            game_total += 1
            y = [x.split() for x in re.findall("(\d+ \w+)", line)] 
            for i in y:
                if int(i[0]) > 12 and i[1] == "red" or int(i[0]) > 13 and i[1] == "green" or int(i[0]) > 14 and i[1] == "blue":
                    imposs += game_total
                    break
            poss += game_total 
    return poss-imposs


def part_two(input):
    with open(input, "r") as f:
        power = 0
        for line in f:
            maxs = {"red": 0, "green": 0, "blue": 0}
            y = [x.split() for x in re.findall("(\d+ \w+)", line)] 
            for i in y:
                if int(i[0]) > maxs["red"] and i[1] == "red":
                    maxs["red"] = int(i[0])
                elif int(i[0]) > maxs["green"] and i[1] == "green":
                    maxs["green"] = int(i[0])
                elif int(i[0]) > maxs["blue"] and i[1] == "blue":
                    maxs["blue"] = int(i[0])
            power += maxs["red"] * maxs["green"] * maxs["blue"]
            print(maxs)

        return power

if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
