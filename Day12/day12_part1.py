import copy
import itertools
"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 12 of 25
      Part 1 of 2 
-------------------------
"""

real_data = True

example = ["???.### 1,1,3",
            ".??..??...?##. 1,1,3",
            "?#?#?#?#?#?#?#? 1,3,1,6",
            "????.#...#... 4,1,1",
            "????.######..#####. 1,6,5",
            "?###???????? 3,2,1"]

# open file and store the input into a list
with open('Day12\day12_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

if real_data:
    input  = lines    
else:
    input = example

# Store the input into two parallel lists, one for the springs and one for the record of damaged springs
springs_list = []
damaged_springs_list = []
for line in input:
    spring = line.split()[0]
    damaged_springs = line.split()[1]
    spring_list = [spr for spr in spring]
    springs_list.append(spring_list)
    damaged_spring = [int(dmg_str) for dmg_str in damaged_springs.split(",")]
    damaged_springs_list.append(damaged_spring)

#print(springs_list)
#print(damaged_springs_list)
# returns true if the arrangement of springs is valid according to the record of damaged springs
def valid_arrangement(springs, damaged_springs):
    group = []
    i = 0
    while (i < len(springs)):
        if springs[i] == '#':
            initial_index = i
            while(i < len(springs) and springs[i] == '#'):
                i += 1
            final_index = i
            length = final_index-initial_index
            group.append(length)
        for j in range(len(group)):
            if len(group) > len(damaged_springs) or group[j] != damaged_springs[j]:
                return False
        i += 1
    if group != damaged_springs:
        return False
    return True

#print(valid_arrangement(['#', '.', '#', '.', '#', '#', '#'], [1, 1, 3]))
#print(valid_arrangement(['.', '#', '.', '.', '.', '#', '.', '.', '.', '#', '#', '#', '#'], [1,1,3]))
#print(valid_arrangement(['.', '#', '.', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#'], [1,3,1,6]))

# returns the number of valid combinations of springs that can be generated from ?s
def calculate_valid_combinations(springs, damaged_springs):
    # Identify the indices of the elements that can change
    question_indices = [i for i, spring in enumerate(springs) if spring == '?']
    # Generate all possible combinations for these elements
    outcomes = ['#', '.']
    combinations = list(itertools.product(outcomes, repeat=len(question_indices)))
    # For each combination, create a copy of the original list and replace the elements at the identified indices
    valid_combinations = 0
    for combination in combinations:
        new_springs = springs.copy()
        for i, index in enumerate(question_indices):
            new_springs[index] = combination[i]
        if valid_arrangement(new_springs, damaged_springs):
            valid_combinations += 1
    return valid_combinations

#print(calculate_valid_combinations(['?', '?', '?', '.', '#', '#', '#'], [1, 1, 3]))
#print(calculate_valid_combinations(['.', '?', '?', '.', '.', '?', '?', '.', '.', '.', '?', '#', '#', '.'], [1,1,3]))

result = 0
for i, spring in enumerate(springs_list):
    result += calculate_valid_combinations(spring, damaged_springs_list[i])
print(f"Part1 Answer: {result}")