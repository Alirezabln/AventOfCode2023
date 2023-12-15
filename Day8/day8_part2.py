"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 8 of 25
      Part 2 of 2 
-------------------------
"""
import math
real_data = True

example = ["LR",
"11A = (11B, XXX)",
"11B = (XXX, 11Z)",
"11Z = (11B, XXX)",
"22A = (22B, XXX)",
"22B = (22C, 22C)",
"22C = (22Z, 22Z)",
"22Z = (22B, 22B)",
"XXX = (XXX, XXX)"]

#open input and remove white spaces
with open("Day8/day8_input.txt", "r", encoding="utf-8") as file:
    input_data = [line.strip() for line in file.readlines() if line.strip()]

if real_data:
    lines = input_data
else: 
    lines = example
    
#sort directions into a list and networks into dict
def sort_directions_networks(lines):
    directions_str = ""
    network_dict = {}
    for i, line in enumerate(lines):
        #first line is always the directions
        if i == 0:
            directions_str = (lines[i])
        else:
            key = str(line.split("=")[0].split()[0])
            first_coordinate = line.split("=")[1].split("(")[1].split(",")[0]
            second_coordinate = line.split("=")[1].split(",")[1].split()[0].split(")")[0]
            value = (first_coordinate, second_coordinate)
            # {AAA : (BBB, CCC)}
            network_dict[key] = value
    return directions_str, network_dict

directions_str, network_dict =  sort_directions_networks(lines)

#Finding all the nodes that have A at their 2nd index and putting them in a list
nodes = []
for key in network_dict:
    if key[2] == 'A':
        nodes.append(key)

#print(nodes)

#Giving that list to a function that determines the steps for each node
def find_next_nodes(nodes):
    steps = []
    for node in nodes:
        step = 0
        element = 0
        end_node = False
        next_step = node
        while not end_node:
            next_steps = network_dict.get(next_step)
            direction = directions_str[element]
            if direction == 'L':
                next_step = next_steps[0]
            else:
                next_step = next_steps[1]
            step += 1
            element += 1
            element %= len(directions_str)
            #Checking each iteration if the 2nd element are all Z
            if next_step[2] == 'Z':
                end_node = True
        steps.append(step)
    return steps

steps = find_next_nodes(nodes)
# Finding the least common multiplier of steps
result = math.lcm(*steps)
#print(steps)
print(result)
