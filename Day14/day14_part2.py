"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 14 of 25
      Part 2 of 2 
-------------------------
"""

from functools import lru_cache
from copy import deepcopy
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
    lines = [line.strip() for line in file.readlines()] 
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

# Recursively slide all the 0 to the west untill encountered by # or other 0
def slide_west(col_index):
    if col_index == 0:
        return
    for row in input:
        if row[col_index] == 'O' and row[col_index-1] == '.':
                row[col_index-1] = 'O' 
                row[col_index] = '.'
    slide_west(col_index-1) 
    
# Recursively slide all the 0 to the south untill encountered by # or other 0
def slide_south(row_index):
    if row_index == len(input)-1:
        return
    row = input[row_index]
    for i, rock in enumerate(row):
        if rock == 'O' and input[row_index+1][i] == '.':
                input[row_index+1][i] = 'O' 
                input[row_index][i] = '.'
    slide_south(row_index+1)
    
# Recursively slide all the 0 to the east untill encountered by # or other 0
def slide_east(col_index):
    if col_index == len(input[0])-1:
        return
    for row in input:
        if row[col_index] == 'O' and row[col_index+1] == '.':
                row[col_index+1] = 'O' 
                row[col_index] = '.'
    slide_east(col_index+1) 


def slide_all():
    for index in range(len(input)):
        slide_north(index)
    for index in range(len(input[0])):
        slide_west(index)
    for index in range(len(input)-1, -1, -1):
        slide_south(index)
    for index in range(len(input[0])-1, -1, -1):
        slide_east(index)

dish_map = []
cycle = []
index = 0
num = 1000000000
hash_map = []
# Stabilize the input
for i in range(num):
    hashed = hash(str(input))
    if hashed in hash_map:
        index = i
        break
    else:
        hash_map.append(hashed)
    slide_all() 
    #print(i)
 
# Find the cycle 
for i in range(num-index):
    check = str(input)
    if check in dish_map:
        #print(f"After {i+1} cycles:")
        #print(hash_map.index(check))
        #for row in input:
            #print(row) 
        #print(len(dish_map))
        break
    else:
        dish_map.append(check) 
        cycle.append(deepcopy(input))
        #print(f"After {i+1} cycles:")
        #for row in input:
            #print(row)
    slide_all() 
 
    
#for items in cycle:
    #print("cycle")
    #for item in items:
        #print(item)
skip_array = (num-index)%len(dish_map)
#print(skip_array)
#for row in cycle[skip_array]:
    #print(row) 
input  = cycle[skip_array]
    
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

print(f"Part2 Answer: {total_load}")
