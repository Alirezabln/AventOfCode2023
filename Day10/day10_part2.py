"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 10 of 25
      Part 2 of 2 
-------------------------
"""

real_data = True

example1 = [
    "...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||.....||.",
    ".||.....||.",
    ".|L-7.F-J|.",
    ".|..|.|..|.",
    ".L--J.L--J.",
    "...........",
]


example2=[".F----7F7F7F7F-7....",
".|F--7||||||||FJ....",
".||.FJ||||||||L7....",
"FJL7L7LJLJ||LJ.L-7..",
"L--J.L7...LJS7F-7L7.",
"....F-J..F7FJ|L7L7L7",
"....L7.F7||L7|.L7L7|",
".....|FJLJ|FJ|F7|.LJ",
"....FJL-7.||.||||...",
"....L---J.LJ.LJLJ..."]

example3 =["FF7FSF7F7F7F7F7F---7",
            "L|LJ||||||||||||F--J",
            "FL-7LJLJ||||||LJL-77",
            "F--JF--7||LJLJ7F7FJ-",
            "L---JF-JLJ.||-FJLJJ7",
            "|F|F-JF---7F7-L7L|7|",
            "|FFJF7L7F-JF7|JL---7",
            "7-L-JL7||F7|L7F-7F7|",
            "L.L7LFJ|||||FJL7||LJ",
            "L7JLJL-JLJLJL--JLJ.L"]


# open input and remove white spaces and store the data
with open("Day10/day10_input.txt", "r", encoding="utf-8") as file:
    input_data = [line.strip() for line in file.readlines() if line.strip()]

if real_data:
    lines = input_data

else:
    lines = example3

# print(lines)

# Find S, the starting position
def find_starting_position(lines):
    for i, line in enumerate(lines):
        if line.find("S") >= 0:
            return i, line.find("S")


x, y = find_starting_position(lines)
# Make list of all the pipes we have visited
pipes_coordinates = [(x, y)]

# print(x,y) # 1, 1
# Have functions for looking up, down, right and left and return the position
def look_right(x, y):
    if lines[x][y] == "-":
        return x, y + 1, "right"
    elif lines[x][y] == "7":
        return x + 1, y, "down"
    elif lines[x][y] == "J":
        return x - 1, y, "up"
    else:
        return None


def look_down(x, y):
    if lines[x][y] == "|":
        return x + 1, y, "down"
    elif lines[x][y] == "J":
        return x, y - 1, "left"
    elif lines[x][y] == "L":
        return x, y + 1, "right"
    else:
        return None


def look_left(x, y):
    if lines[x][y] == "-":
        return x, y - 1, "left"
    elif lines[x][y] == "L":
        return x - 1, y, "up"
    elif lines[x][y] == "F":
        return x + 1, y, "down"
    else:
        return None


def look_up(x, y):
    if lines[x][y] == "|":       
        return x - 1, y, "up"
    elif lines[x][y] == "7":
        return x, y - 1, "left"
    elif lines[x][y] == "F":
        return x, y + 1, "right"
    else:
        return None


# Find the first direction to proceed
def find_first_direction(x, y):
    if look_right(x, y + 1):
        pipes_coordinates.append((x, y +1))
        return look_right(x, y + 1)
    elif look_down(x + 1, y):
        pipes_coordinates.append((x+1, y))
        return look_down(x + 1, y)
    elif look_up(x - 1, y):
        pipes_coordinates.append((x -1, y))
        return look_up(x - 1, y)
    else:
        pipes_coordinates.append((x, y-1))
        return look_left(x, y - 1)


# Find the first position to proceed
x, y, direction = find_first_direction(x, y)
# print(x, y, direction)
pipes_coordinates.append((x, y))

# while we are not back to S, keep looking
while lines[x][y] != "S":
    if direction == "right":
        x, y, direction = look_right(x, y)
    elif direction == "left":
        x, y, direction = look_left(x, y)
    elif direction == "up":
        x, y, direction = look_up(x, y)
    elif direction == "down":
        x, y, direction = look_down(x, y)
    pipes_coordinates.append((x, y))
  
print(pipes_coordinates)

# A function that returns a times that we have visited pipes casting a ray straight up
def times_visited(x, y):
    times_visited = 0 # NE, SE, SW, NW, N, E, S, W
    i = 1
    if (x, y) in pipes_coordinates:
        return times_visited
    while x-i >= 0 and x - i < len(lines):
        if (x-i , y) in pipes_coordinates:
            if lines[x-i][y] == "L":
                while x-i >= 0:
                    if lines[x-i][y] == "F" or lines[x-i][y] == "S":
                        break
                    if lines[x-i][y] == "7":
                        if (x-i , y) in pipes_coordinates: 
                            times_visited +=1  
                            break
                    i += 1
            elif lines[x-i][y] == "J":
                while x-i >= 0 and lines[x-i][y]: 
                    if lines[x-i][y] == "7":
                        break
                    if lines[x-i][y] == "F" or lines[x-i][y] == "S":
                        if (x-i , y) in pipes_coordinates:
                            times_visited +=1
                            break
                    i += 1
            elif lines[x-i][y] == "-":
                times_visited +=1
            #print(x,y)
        i+= 1
    return times_visited

# A function that determines if a number is odd
def odd(num):
    if num == 0:
        return False
    if num % 2 == 0:
            return False
    return True

# Iterate over all the tiles and count the ones that diagonally have been visited by pipes odd number of times
result = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        times_visited_pipes = times_visited(i, j)
        #If a line from a point is enclosed by a loop then a ray cast from that point to any direction must cross
        #the loop odd number of times
        if odd(times_visited_pipes):
            result += 1
            #print(result)
          
print(f"Part2 Answer: {result}")
