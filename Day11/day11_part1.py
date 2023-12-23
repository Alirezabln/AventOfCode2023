"""
-------------------------
    Advent of Code 2023
    Alireza Bolourian
    Challenge 11 of 25
      Part 1 of 2 
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

# A function that inserts rows and columns of dots to rows and columns without stars
def expanded_space(space, rows,cols):
    i = 0
    for row in rows:
        dots = '.' * len(space[0])
        space.insert(row+i, dots)
        i += 1
    j = 0
    for col in cols:
        for i in range(len(space)):
            space[i] = space[i][:col+j] + '.' + space[i][col+j:]
        j += 1
    return space

expanded_space = expanded_space(input, rows_without_stars, cols_without_stars)
#print(expanded_space)

# write the list into a file
with open('Day11\day11_expanded.txt', 'w') as file:
    for line in expanded_space:
        file.write(line + '\n')
        
# A function that stores the position of star in a list
def get_star_positions(space):
    star_positions = []
    for i in range(len(space)):
        for j in range(len(space[0])):
            if space[i][j] == '#':
                star_positions.append((i,j))
    return star_positions

star_positions = get_star_positions(expanded_space)
#print(star_positions)

# A function that return the sum of shortest distances between a point and the other points
def get_distance(point, points):
    distances = []
    for p in points:
        distance = abs(point[0] - p[0]) + abs(point[1] - p[1])
        distances.append(distance)
    return sum(distances)

# Count the sum of shoertest distances between each pair of stars, couting each pair only once
distance = 0
for i in range(len(star_positions)):
    distance += get_distance(star_positions[i], star_positions[i:])
print(f"Part1 Answer: {distance}")