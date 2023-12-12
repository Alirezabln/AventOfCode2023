"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 6 of 25
      Part 2 of 2
-------------------------
"""

real_data = True

example = ["Time:      7  15   30",
        "Distance:  9  40  200"]

with open("Day6/day_6_input.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

if real_data:
    lines = data
else:
    lines = example

def time_distance(lines):
    time_list = int("".join([num for num in lines[0].split(":")[1].split()]))
    distance_list = int("".join([num for num in lines[1].split(":")[1].split()]))
    return time_list, distance_list

def number_of_ways(time, distance):
    number = 0
    for j in range(time):
        if j*(time-j) > distance:
            number += 1
    return number

time, distance = time_distance(lines)
#print(time)
#print(distance)

total_number = number_of_ways(time, distance)
print(total_number)