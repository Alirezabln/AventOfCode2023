"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 11 of 25
      Part 2 of 2 
-------------------------
"""

real_data = True

example = ["...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#....."]

# open file and store the input into a list
with open('Day11\day11_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

if real_data:
    input  = lines
    
else:
    input = example
    
# A function that returns row numbers that have no stars in them
def get_rows_without_stars(rows):
    rows_without_stars = []
    for i, row in enumerate(rows):
        if not '#' in row:
            rows_without_stars.append(i)
    return rows_without_stars

# A function that returns column numbers that have no stars in them
def get_cols_without_stars(rows):
    cols_without_stars = []
    for i in range(len(rows[0])):
        col_without_stars = True
        for j in range(len(rows)):
            if rows[j][i] == '#':
                col_without_stars = False
                break
        if col_without_stars == True:
            cols_without_stars.append(i)
    return cols_without_stars

rows_without_stars = get_rows_without_stars(input)
cols_without_stars = get_cols_without_stars(input)

#print(rows_without_stars)
#print(cols_without_stars)
        
# A function that stores the modified positions of stars into a list
def get_star_positions(space, rows_expand, cols_expand):
    star_positions = []
    for i in range(len(space)):
        for j in range(len(space[0])):
            if space[i][j] == '#':
                x = i
                y = j
                expansion_multplier = 1000000
                for row in rows_expand:
                    if row < i:
                        x += expansion_multplier-1
                    else: break
                for col in cols_expand:
                    if col < j:
                        y += expansion_multplier-1
                    else: break
                star_positions.append((x,y))
    return star_positions

star_positions = get_star_positions(input, rows_without_stars, cols_without_stars)
#print(star_positions)

# A function that return the sum of shortest distances between a point and the other points
def get_distance(point, points):
    distances = []
    for p in points:
        distance = abs(point[0] - p[0]) + abs(point[1] - p[1])
        distances.append(distance)
    return sum(distances)

#print(star_positions)

# Count the sum of shortest distances between each pair of stars, counting each pair only once
shortest_distance = 0
for i in range(len(star_positions)):
    shortest_distance += get_distance(star_positions[i], star_positions[i:])
    #print(shortest_distance)
print(f"Part2 Answer: {shortest_distance}")