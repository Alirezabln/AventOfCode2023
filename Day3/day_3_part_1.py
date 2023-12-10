"""
---------------------------
    Advent of code 2023
    Alireza Bolourian
    Challenge 3 of 25
        Part 1
---------------------------    
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
# Part 1
summation = 0 # pylint: disable=C0103
with open("Puzzle3/Puzzle3Input.txt", "r", encoding ="utf-8") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        j = 0
        while (j < len(line)):
            if line[j].isdigit():
                startIndex = j
                valid = False
                while (line[j].isdigit()):
                    for a in range(-1,2):
                        for b in range(-1,2):
                            if not(i+a < 0 or i+a >= len(lines) or j+b< 0 or j+b >= len(line)):
                                if ord(lines[i+a][j+b]) != 46 and ord(lines[i+a][j+b]) != 10:
                                    if ord(lines[i+a][j+b]) < 48 or ord(lines[i+a][j+b]) > 57:
                                        valid = True
                    endIndex = j
                    j += 1
                if valid:
                    num = int(line[startIndex:endIndex+1])
                    summation += num
            j += 1
print(summation)

