"""
Time:      7  15   30
Distance:  9  40  200
"""

def part_one(input):
    with open(input, "r") as f:
        time, distance = [x.split(":")[1].strip().split() for x in f.read().splitlines()]
        races = list(zip(time,distance))
        
        win_total = 1

        # iterate with time
        for race in races:
            wins = 0
            for t in range(1, int(race[0]) + 1):
                if t * (int(race[0]) - t) > int(race[1]):
                    wins += 1 
            win_total *= wins 

        print(win_total)
            

def part_two(input):
    with open(input, "r") as f:
        time, distance = [x.split(":")[1].replace(" ","") for x in f.read().splitlines()]
       

        
        wins = 0
        # iterate with time
        # this is realllllllly slow
        for t in range(1, int(time) + 1):
            if t * (int(time) - t) > int(distance):
                wins += 1 

        print(wins)
                 


if __name__ == "__main__":
    part_one("input.txt")
    part_two("input.txt")
