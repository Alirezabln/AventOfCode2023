"""
--------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 6 of 25
      Part 1 of 2
--------------------------
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

def create_lists(lines):
    time_list = [int(num) for num in lines[0].split(":")[1].split()]
    distance_list = [int(num) for num in lines[1].split(":")[1].split()]
    return time_list, distance_list

def number_of_ways(time, distance):
    number = 0
    for j in range(time):
        if j*(time-j) > distance:
            number += 1
    return number

times, distances = create_lists(lines)
#print(times)
#print(distances)

total_number = 1
for i, race in enumerate(times):
    total_number *= number_of_ways(race, distances[i])
print(total_number)
