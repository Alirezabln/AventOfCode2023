"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 2 of 25
        Part 2
-------------------------
"""

example = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

sum = 0
with open("Puzzle2Input.txt", "r") as file:
    lines = file.readlines()
    for line in lines: 
        red = 0
        blue = 0
        green = 0
        power = 0
        s = line.split(":")
        sets = s[1].split(";")
        for set in sets:
            cubes = set.split(",") 
            for cube in cubes:
                num = int(cube.split()[0])
                match cube.split()[1]:
                    case "red":
                        if num > red:
                            red = num
                    case "blue":
                        if num > blue:
                            blue = num
                    case "green":
                        if num > green:
                            green = num
        power = red*blue*green
        sum += power

print(sum)