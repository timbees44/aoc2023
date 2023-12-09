"""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

def part_one(input):
    with open(input, "r") as f:
        # unpack the input with first sections assigned to seeds and the rest assigned to block using *
        seeds, *blocks = f.read().split("\n\n")
        # tidy up seeds and put in list
        seeds = list(map(int, seeds.split(":")[1].split()))
        
        # iterate through blocks
        for block in blocks:
            # create ranges for each block section
            ranges = [] 
            # split out and tidy blocks 
            for line in block.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))
            # create new variable for seeds so that we don't alter the original
            new = []
            # iterate through seeds for each block
            for x in seeds:
                # apply ranges in problem the seed has to be inbetween the source start range and the source start range + range length
                for a, b, c in ranges:
                    if b <= x < b + c:
                        # append corresponding value which is x - source range start value plus range destination
                        new.append(x - b + a)
                        # break out frist time this occurs
                        break
                else:
                    # if for loop yields nothing then we just append x and try again
                    new.append(x)

            seeds = new
    
        print(min(seeds))


if __name__ == "__main__":
    part_one("input.txt")
