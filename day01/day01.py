
def part_one(input):
    with open(input, "r") as f:
        total = 0
        for line in f:
            sub = [x for x in line if x.isnumeric()]
            total += int(sub[0] + sub[-1])
            sub = [] 
    return total

# a nicer way to do part two would be to use regex with a positive look ahead.
def part_two(input):
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    with open(input, "r") as f:
        total = 0
        sub = []
        for line in f:
            for k, v in words.items():
                if k in line:
                    line = line.replace(k, k+str(v)+k)
            for i in line:
                if i.isnumeric():
                    sub.append(i) 
            total += int(sub[0] + sub[-1])
            sub = [] 
    return total

if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
    
