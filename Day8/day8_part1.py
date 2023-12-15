"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 8 of 25
      Part 1 of 2 
-------------------------
"""

import sys
real_data = True

example = ["LLR",
"AAA = (BBB, BBB)",
"BBB = (AAA, ZZZ)",
"ZZZ = (ZZZ, ZZZ)"]

#open input and remove white spaces
with open("Day8/day8_input.txt", "r", encoding="utf-8") as file:
    input_data = [line.strip() for line in file.readlines() if line.strip()]

if real_data:
    lines = input_data
else: 
    lines = example
    
#print(lines)
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
            #print(first_coordinate)
            second_coordinate = line.split("=")[1].split(",")[1].split()[0].split(")")[0]
            #print(second_coordinate)
            value = (first_coordinate, second_coordinate)
            # {AAA : (BBB, CCC)}
            network_dict[key] = value
    return directions_str, network_dict

directions_str, network_dict =  sort_directions_networks(lines)
#print(directions_str)
#print(network_dict)
#print(sys.getrecursionlimit())
#a recursive function that determines the next network based on the direction list
#track the steps as the direction list is traversed 
steps = 0
element = 0
node = "AAA"
def follow_next_node(start_node, element):
    element %= len(directions_str)
    if start_node == "ZZZ":
        return 0
    else: 
        next_steps = network_dict.get(start_node)
        if directions_str[element] == 'L':
            steps = 1 + follow_next_node(next_steps[0], element+1)
        else: 
            steps = 1 + follow_next_node(next_steps[1], element+1)  
    return steps

#steps = follow_next_node(node, element)
#print(steps)
#non recursive way because the maxium recursion depth is reached
while(node != "ZZZ"):
    next_steps = network_dict.get(node)
    if directions_str[element] == 'L':
        node = next_steps[0]
    else: 
        node = next_steps[1]
    steps += 1
    element += 1
    element %= len(directions_str)
print(steps)
