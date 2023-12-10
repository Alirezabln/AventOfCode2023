"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 1 of 25
        Part 1
-------------------------
"""

count  = 0
num_word_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1", 
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

with open("Puzzle1.txt", 'r', encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        num = ''
        lowest_index = 99
        highest_index = -1
        left = ""
        right = ""
        for key, value in num_word_dict.items():
            check_sentence = line
            check = check_sentence.find(key)
            while check >= 0:
                if check < lowest_index:
                    lowest_index = check
                    left = value
                if check > highest_index:
                    highest_index = check
                    right = value 
                check = check_sentence.find(key, check+1)
        count += int(num)

print(count)

