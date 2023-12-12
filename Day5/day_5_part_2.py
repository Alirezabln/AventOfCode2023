"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 5 of 25
      Part 2 of 2
-------------------------
"""

real_data = True

example = ["seeds: 79 14 55 13",
"seed-to-soil map:",
"50 98 2",
"52 50 48",
"soil-to-fertilizer map:",
"0 15 37",
"37 52 2",
"39 0 15",
"fertilizer-to-water map:",
"49 53 8",
"0 11 42",
"42 0 7",
"57 7 4",
"water-to-light map:",
"88 18 7",
"18 25 70",
"light-to-temperature map:",
"45 77 23",
"81 45 19",
"68 64 13",
"temperature-to-humidity map:",
"0 69 1",
"1 0 69",
"humidity-to-location map:",
"60 56 37",
"56 93 4"]

with open("Day5/day_5_Input.txt", "r", encoding = "utf-8") as file:
    data = [line.strip() for line in file if line.strip()]

if real_data:
    lines = data
else:
    lines = example

def createLists(lines):
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    numberOfLists = 0
    for i, line in enumerate(lines):
        if numberOfLists < 8:
            if ':' in line:
                if numberOfLists == 0:
                    nums = line.split(":")[1]
                    seeds = [int(num) for num in nums.split()]
                else:
                    temp = []
                    j = i + 1
                    while j < len(lines) and lines[j].find(':') == -1:
                        temp1 = [int(num) for num in lines[j].split()]
                        temp.extend(temp1)
                        j += 1
                    if numberOfLists == 1:
                        seed_to_soil = temp     
                    if numberOfLists == 2:
                        soil_to_fertilizer = temp
                    if numberOfLists == 3:
                        fertilizer_to_water = temp
                    if numberOfLists == 4:
                        water_to_light = temp
                    if numberOfLists == 5:
                        light_to_temperature = temp
                    if numberOfLists == 6:
                        temperature_to_humidity = temp
                    if numberOfLists == 7:
                        humidity_to_location = temp
                numberOfLists += 1
    return seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location

seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location  = createLists(lines)

#print(f"Seeds: {seeds}")
#print(f"Seed_to_soil: {seed_to_soil}")
#print(f"Soil_to_fertilizer: {soil_to_fertilizer}" )
#print(f"Fertilizer_to_water: {fertilizer_to_water}")
#print(f"Water_to_light:{water_to_light}")
#print(f"light_to_temperature:{light_to_temperature}")
#print(f"temperature_to_humidity:{temperature_to_humidity}")
#print(f"humidity_to_location:{humidity_to_location}")

def mapping(list1, list2):
    mapped_list = []
    lenList2 = len(list2)//3
    for num in list1:
        mapped_num = num
        for j in range(lenList2):
            if num >= list2[j*3 + 1] and num < list2[j*3 + 1] + list2[j*3 + 2]:
                mapped_num = list2[j*3] + (num - list2[j*3 + 1])
        mapped_list.append(mapped_num)
    return mapped_list

def convertToRange(list):
    lenList = len(list)//2
    converted_to_range = []
    for i in range(lenList):
        for j in range(list[i*2 + 1]):
            converted_to_range.append(list[i*2] + j)
    return converted_to_range
    
mapped_list = convertToRange(seeds[:2])
print("step 1 of 8")
mapped_list = mapping(mapped_list, seed_to_soil)
print("step 2 of 8")
mapped_list = mapping(mapped_list, soil_to_fertilizer)
print("step 3 of 8")
mapped_list = mapping(mapped_list, fertilizer_to_water)
print("step 4 of 8")
mapped_list = mapping(mapped_list, water_to_light)
print("step 5 of 8")
mapped_list = mapping(mapped_list, light_to_temperature)
print("step 6 of 8")
mapped_list = mapping(mapped_list, temperature_to_humidity)
print("step 7 of 8")
mapped_list = mapping(mapped_list, humidity_to_location)
print("step 8 of 8!")
print(min(mapped_list))