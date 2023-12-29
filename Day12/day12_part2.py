"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 12 of 25
      Part 2 of 2 
-------------------------
https://advent-of-code.xavd.id/writeups/2023/day/12/ Thank you for the help!
"""
from functools import lru_cache
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
    spring, damaged_springs = line.split()
    unfoldedSpring = '?'.join([spring] * 5)
    springs_list.append(unfoldedSpring)
    damaged_spring = tuple(int(dmg_str) for dmg_str in damaged_springs.split(","))
    damaged_spring *= 5
    damaged_springs_list.append(damaged_spring)

# Recursively find valid combinations
@lru_cache #Python Maximization
def valid_combinations(springs, damaged_springs):
    # Base cases
    if not springs:
        return len(damaged_springs) == 0
    if not damaged_springs:
        return '#' not in springs

    spring, restOfSprings = springs[0], springs[1:]
    # General case for dot
    if spring == '.':
        return valid_combinations(restOfSprings, damaged_springs)
    # General case for '#'
    group = damaged_springs[0]
    if spring == '#' and len(springs) >= group and all(char != '.' for char in springs[:group]) and (len(springs) == group or springs[group] != '#'):
        return valid_combinations(springs[group+1:], damaged_springs[1:])
    # General case for '?'
    if spring == '?':
        return valid_combinations('#' + restOfSprings, damaged_springs) + valid_combinations('.' + restOfSprings, damaged_springs)
    
    return 0

result = 0
for i, record in enumerate(springs_list):
    result += valid_combinations(record, damaged_springs_list[i])
print(result)