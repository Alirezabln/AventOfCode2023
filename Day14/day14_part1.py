"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 14 of 25
      Part 1 of 2 
-------------------------
"""

real_data = True

example = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#...."
]


# open file and store the input into a list
with open('Day14\day14_input.txt', 'r') as file: 
    lines = file.readlines() # split the file content by empty lines
# Convert the input into a list of list
if real_data:
    input  = [list(line) for line in lines]  
else:
    input = [list(line) for line in example]

# Recursively slide all the 0 to the north untill encountered by # or other 0 
def slide_north(row_index):
    if row_index == 0:
        return
    row = input[row_index]
    for i, rock in enumerate(row):
        if rock == 'O' and input[row_index-1][i] == '.':
                input[row_index-1][i] = 'O' 
                input[row_index][i] = '.'
    slide_north(row_index-1)


for index in range(len(input)):
    slide_north(index)

#print(input)
    
# Calculate the load of the row
def calculate_load(row_index):
    load = 0
    for rock in input[row_index]:
        if rock == 'O':
            load += row_index+1
    return load

# Calculate the total load
input.reverse()
total_load = 0
for i in range(len(input)):
    total_load += calculate_load(i)

print(f"Part1 Answer: {total_load}")
