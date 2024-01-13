"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 15 of 25
      Part 1 of 2 
-------------------------
"""

real_data = True

example1 = "HASH"
example2 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

# open file and store the input into a list using "," as delimiter
with open('Day15\day15_input.txt', 'r') as file: 
    line = file.readline()
    items = line.split(",")
    
# Use the real data or the example
if real_data:
    input  = items 
else:
    input = example2.split(",")
    
#print(input) 

# A function that calculates the hash value of the string
def hash_value(str):
    current_value = 0
    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

#print(hash_value(example1))
result = 0
for item in input:
    result += hash_value(item)
    
print(f"Part1 Answer: {result}")