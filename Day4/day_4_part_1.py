"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 4 of 25
        Part 1
-------------------------
"""

real_data = True

example = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

with open("Day4/day_4_Input.txt", "r", encoding = "utf-8") as file:
    data = file.readlines()

if real_data:
    lines = data
else:
    lines = example

def createLists(line):
    win_num = [int(num) for num in line.split(":")[1].split("|")[0].split()]
    my_num = [int(num) for num in line.split(":")[1].split("|")[1].split()]
    return win_num, my_num

def calculatePoints(win_nums, my_nums):
    points = 0
    for win_num in win_nums:
        for my_num in my_nums:
            if win_num == my_num:
                if points  == 0:
                    points = 1
                else:
                    points *= 2
    return points

points = 0
for line in lines:
    wining_num, my_num = createLists(line)
    points += calculatePoints(wining_num, my_num)
print(points)
