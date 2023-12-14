"""
--------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 2 of 25
        Part 1
--------------------------
"""
example = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
sum = 0
bag = {
    "red" : 12,
    "green" : 13,
    "blue" : 14}
with open("Puzzle2Input.txt", "r") as file:
    lines = file.readlines()
    for line in lines: 
        s = line.split(":")
        id  = int(s[0].split(" ")[1])
        sets = s[1].split(";")
        valid  = True
        for set in sets:
            cubes = set.split(",") 
            for cube in cubes:
                for key, value in bag.items():
                    if cube.find(key) > 0:
                        if int(cube.split()[0]) > value:
                            valid = False
        if valid == True:
            sum += id
        

print(sum)

