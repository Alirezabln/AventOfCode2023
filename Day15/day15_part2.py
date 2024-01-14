"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 15 of 25
      Part 2 of 2 
-------------------------
"""

real_data = True

example1 = "rn"
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

# Boxes list with 256 lists inside
boxes = [[] for i in range(256)]

# A function that calculates the hash value of the string
def hash_value(str):
    current_value = 0
    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

#print(hash_value(example1))
# A function that finds the label and focal length from the item and determines the operation
def initialization(item):
    if "=" in item:
        label = item.split("=")[0]
        focal_length = int(item.split("=")[1])
        hash_label = hash_value(label)
        equal_operation(hash_label, label, focal_length)
    else:
        label = item.split("-")[0]
        hash_label = hash_value(label)
        minus_operation(hash_label, label)
    
# A function that for the = operation
def equal_operation(hash_label, label, focal_length):
    for i in range(len(boxes[hash_label])):
        # If label present in the box, update the focal length
        if label == boxes[hash_label][i][0]:
            boxes[hash_label][i][1] = focal_length
            break
        # If label not present in the box, add it to the box
    else: 
        new_box = [label, focal_length]
        boxes[hash_label].append(new_box)

# A function that for the - operation
def minus_operation(hash_label, label):
    for i in range(len(boxes[hash_label])):
        # If label present in the box, remove it from the box
        if label == boxes[hash_label][i][0]:
            boxes[hash_label].pop(i)
            break
        
# A function that calculates the focusing power of the box
def focusing_power(i, box):
    power = 0
    for j, lens in enumerate(box):
        # (one plus the index of the box) * (one plus the index of the lens) * (the focal length of the lens) 
            power += ((i+1)*(j+1)*lens[1])
    return power

# Main loop
result = 0
for item in input:
    initialization(item)
    
for i, box in enumerate(boxes):
    if box != []:
        result += focusing_power(i, box)
       
#print(boxes)
print(f"Part2 Answer {result}")
