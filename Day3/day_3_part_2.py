"""
----------------------------
    Advent of code 2023
    Alireza Bolourian
    Challenge 3 of 25
        Part 2
----------------------------   
"""

example = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."
]

# Part2

gears = []
adjacent = 0
num1 = num2  = 0

def start(lines, i, a, backwards):
    while(lines[i+a][backwards].isdigit()):
        #print(lines[i+a][backwards])
        startIndex = backwards
        backwards -= 1
    return startIndex

def end(lines, i, j, a, forward):
    while(lines[i+a][forward].isdigit()):
        #print(lines[i+a][forward])
        endIndex = forward
        b = forward - j
        forward += 1
    return b,endIndex

with open("Puzzle3/Puzzle3Input.txt", "r", encoding = "utf-8") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        j = 0
        while (j < len(line)):
            if lines[i][j] == '*':
                adjacent = 0
                for a in range(-1,2):
                    b = -1
                    while b < 2:
                        if not(i+a < 0 or i+a >= len(lines) or j+b< 0 or j+b >= len(lines)):
                            if lines[i+a][j+b].isdigit():
                                adjacent += 1
                                backwards = j+b
                                forward = j+b
                                startIndex = start(lines, i, a, backwards)
                                b, endIndex = end(lines, i, j, a, forward)
                                if adjacent == 1:
                                    num1 = int(lines[i+a][startIndex:endIndex+1])
                                    #print(lines[i+a][startIndex:endIndex+1])
                                if adjacent == 2:
                                    num2 = int(lines[i+a][startIndex:endIndex+1])
                                    #print(lines[i+a][startIndex:endIndex+1])
                        b += 1
            if adjacent == 2:
                #print(num1)
                #print(num2)
                gears.append(num1 * num2)
                adjacent = 0
                num1 = num2 = 0
            j += 1
print(gears)
print(sum(gears))
