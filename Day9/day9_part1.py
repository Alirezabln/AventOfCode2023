"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 9 of 25
      Part 1 of 2 
-------------------------
"""

real_data = True

example = ["0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45"]

#open input and remove white spaces
with open("Day9/day9_input.txt", "r", encoding="utf-8") as file:
    input_data = [line.strip() for line in file.readlines() if line.strip()]

# Store each as an element of a list of a list[[]]
if real_data:
    lines = [[[int(num) for num in line.split()]] for line in input_data] 
else: 
    lines = [[[int(num) for num in line.split()]] for line in example]
    
# [[[]], [[]], [[]]]
#print(lines)
#print(lines[0])
    
# Generate the difference list and append the list to the coressponding list[[]] unill 0 list was found
def append_difference_lists(lines):
    for line in lines:
        #[],
        j = 0
        all_zero_nums = False
        while not all_zero_nums:
            history_line = line[j]
            new_list = []
            for i in range(len(history_line)-1):
                num1 = history_line[i]
                num2 = history_line[i+1]
                difference = num2 - num1
                new_list.append(difference)
            if all(num == 0 for num in new_list):
                all_zero_nums = True
            line.append(new_list)
            j += 1
                
append_difference_lists(lines)
#print(lines)

# Go backwards and append values to list[[]] until the value for history is found
def calculate_history_value(history_line):#[[],[],[]]
    history_line[len(history_line)-1].append(0) 
    for i in range(len(history_line)-1, 0, -1):
        num = history_line[i][-1] + history_line[i-1][-1]
        history_line[i-1].append(num)
    return history_line[0][-1]
    
result = 0
for line in lines:
    result += calculate_history_value(line)
    
print(f"Part 1 Answer: {result}")
