"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 10 of 25
      Part 1 of 2 
-------------------------
"""

real_data = True

example1 = [".....",
            ".S-7.",
            ".|.|.",
            ".L-J.",
            "....."]

example2 = ["..F7.",
            ".FJ|.",
            "SJ.L7",
            "|F--J",
            "LJ..."]

#open input and remove white spaces and store the data
with open("Day10/day10_input.txt", "r", encoding="utf-8") as file:
    input_data = [line.strip() for line in file.readlines() if line.strip()]
    
if real_data:
    lines = input_data
   
else:
    lines = example2
    
#print(lines)

# Find S, the starting position
def find_starting_position(lines):
    for i, line in enumerate(lines):
        if line.find('S') >= 0:
            return i, line.find('S')
        
x, y = find_starting_position(lines)
#print(x,y) # 1, 1    
# Have functions for looking up, down, right and left and return the position
def look_right(x, y):
    if lines[x][y] == '-':
       return x, y + 1, 'right'
    elif lines[x][y] == '7': 
        return x + 1, y, 'down'
    elif lines[x][y] == 'J':
        return x-1, y, 'up'
    else:
        return None
    
def look_down(x, y):
    if lines[x][y] == '|':
        return x+1, y, 'down'
    elif lines[x][y] == 'J':
        return x, y-1, 'left'
    elif lines[x][y] == 'L':
        return x, y+1, 'right'
    else:
        return None
    
def look_left(x, y):
    if lines[x][y] == '-':
       return x, y-1, 'left'
    elif lines[x][y] == 'L':
        return x-1, y, 'up'
    elif lines[x][y] == 'F':
        return x+1, y, 'down'
    else:
        return None
    
def look_up(x, y):
    if lines[x][y] == '|':
        return x-1, y, 'up'
    elif lines[x][y] == '7':
        return x, y-1, 'left'
    elif lines[x][y] == 'F':
        return x, y+1, "right"
    else:
        return None


def find_first_direction(x, y):
    if look_right(x, y+1):
        return look_right(x, y+1)
    elif look_down(x+1, y):
        return look_down(x+1, y)
    elif look_up(x+1, y):
        return look_up(x+1, y)
    else:
        return look_left(x, y-1)

# Find the first position to proceed
x, y, direction = find_first_direction(x, y)
#print(x, y, direction)
# Have a loop that iterates until we come back to S, and record the length
length = 2

while(lines[x][y] != 'S'):
    if direction == 'right':
        x, y, direction = look_right(x, y)
    elif direction == 'left':
        x, y, direction = look_left(x, y)
    elif direction == 'up':
        x, y, direction = look_up(x, y)
    elif direction == 'down':
        x, y, direction = look_down(x, y)
    length += 1
    
# The farthest distance is length/2
print(f"Part1 Answer: {length//2}")

