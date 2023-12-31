"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 13 of 25
      Part 1 of 2 
-------------------------
"""

real_data = True

example = [["#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#."],
            ["#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#"]]

# open file and store the input into a list of list
with open('Day13\day13_input.txt', 'r') as file: 
    data = file.read().split('\n\n') # split the file content by empty lines
    lines = [item.split('\n') for item in data] # split each line by new line character

if real_data:
    input  = lines    
else:
    input = example

#print(input)
# Function that determines if vertical reflection exists and returns the index to the left of the reflection
def vertical_reflection(pattern):
    for j in range(len(pattern[0])-1):
        # How many columns to check, ignore the rest
        col = j+1 if len(pattern[0]) // 2 > j+1 else len(pattern[0])-j-1
        # Check if the pattern is mirrored 
        if all(pattern[i][j+k+1] == pattern[i][j-k] for k in range(col) for i in range(len(pattern))): # check if the pattern is mirrored
            return j+1
    return 0

#print(vertical_reflection(example[1]))

# Function that determines if horizontal reflection exists and returns the rows above the reflection
def horizontal_reflection(pattern):
    for i in range(len(pattern)-1):
        # How many rows to check, ignore the rest
        row = i+1 if len(pattern) // 2 > i+1 else len(pattern)-i-1
        # Check if the pattern is mirrored 
        if all(pattern[i+k+1][j] == pattern[i-k][j] for k in range(row) for j in range(len(pattern[0]))): # check if the pattern is mirrored
            return i+1
    return 0

#print(horizontal_reflection(example[1]))

result = 0
for pattern in input:
    # Check for vertical reflection
    vertical = vertical_reflection(pattern)
    # Check for horizontal reflection
    horizontal = horizontal_reflection(pattern)
    # Calculate the results
    if vertical:
        result += vertical
    else: 
        result += horizontal*100

print(result)
