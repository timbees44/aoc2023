"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

"""
taken from HyperNutrino as I had difficulty working with grids:
    - https://www.youtube.com/watch?v=ZFGX5D9mi-4
"""

def part_one(input):
    with open(input, "r") as f:
        grid = f.read().splitlines()
        cs = set()
        
        #iterate through rows (lines in grid)
        for r, row in enumerate(grid):
            # iterate through column characters using rows as enum argument
            for c, ch in enumerate(row):
                # check if character is digit or . - we don't care about these
                if ch.isdigit() or ch == ".":
                    continue
                # check row above, current row and row below
                for cur_row in [r-1, r, r+1]:
                    # check colum left, current col and right
                    for cur_col in [c-1, c, c+1]:
                        # make sure row and colums are in bounds 
                        if cur_row < 0 or cur_row >= len(grid) or cur_col < 0 or cur_col >= len(grid[cur_row]) or not grid[cur_row][cur_col].isdigit(): 
                            continue
                        # iterate backwards by one through columns until starting digit is found for each number
                        while cur_col > 0 and grid[cur_row][cur_col - 1].isdigit():
                            cur_col -= 1
                        # add coordinates
                        cs.add((cur_row, cur_col))

        num_list = []

        #iterate through coordinates
        for r, c in cs:
            s = ""
            # ensure that we don't go out of bounds and check that each iteration is digit to build full number
            while c < len(grid[r]) and grid[r][c].isdigit():
                # add string value of digit to s
                s += grid[r][c]
                c += 1
            
            # append full s value to num_list as an int
            num_list.append(int(s))
        
        print(sum(num_list))



def part_two(input):
    with open(input, "r") as f:
        grid = f.read().splitlines()
        total = 0 
        #iterate through rows (lines in grid)
        for r, row in enumerate(grid):
            # iterate through column characters using rows as enum argument
            for c, ch in enumerate(row):
                # check if character is digit or . - we don't care about these
                if ch != "*":
                    continue


                cs = set()


                # check row above, current row and row below
                for cur_row in [r-1, r, r+1]:
                    # check colum left, current col and right
                    for cur_col in [c-1, c, c+1]:
                        # make sure row and colums are in bounds 
                        if cur_row < 0 or cur_row >= len(grid) or cur_col < 0 or cur_col >= len(grid[cur_row]) or not grid[cur_row][cur_col].isdigit(): 
                            continue
                        # iterate backwards by one through columns until starting digit is found for each number
                        while cur_col > 0 and grid[cur_row][cur_col - 1].isdigit():
                            cur_col -= 1
                        # add coordinates
                        cs.add((cur_row, cur_col))


                if len(cs) != 2:
                    continue

                num_list = []

                #iterate through coordinates
                for row, col in cs:
                    s = ""
                    # ensure that we don't go out of bounds and check that each iteration is digit to build full number
                    while col < len(grid[row]) and grid[row][col].isdigit():
                        # add string value of digit to s
                        s += grid[row][col]
                        col += 1
                    
                    # append full s value to num_list as an int
                    num_list.append(int(s))
                
                total += num_list[0] * num_list[1]

        print(total)


if __name__ == "__main__":
    part_one("input.txt")
    part_two("input.txt")
