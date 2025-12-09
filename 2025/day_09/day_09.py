part1 = 0
part2 = 0

# Parse the input file, line by line
input = [tuple(map(int, line.strip().split(","))) for line in open("day_09_input.txt", 'r')]

# Iterate through pairwise (compare every line with every other line)
for i in range(len(input)):
    for j in range(i + 1, len(input)):

        # Calculate area as delta of (x,y) points
        area = (abs(input[i][0] - input[j][0]) + 1) * (abs(input[i][1] - input[j][1]) + 1)

        # If calculated area exceeds current best, update part1
        if area > part1:
            part1 = area

print("Part 1:", part1)
print("Part 2:", part2)
