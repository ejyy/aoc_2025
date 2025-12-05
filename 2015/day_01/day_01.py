part1 = 0
part2 = 0

# Parse the input file
input = [data for data in open("day_01_input.txt", 'r').read().strip()]

# Run through, adding / subtracting based on bracket
for x in input:
    if x == "(":
        part1 += 1
    if x == ")":
        part1 -= 1

# Keep a running tally of floor
floor = 0
for i, x in enumerate(input):
    if x == "(":
        floor += 1
    if x == ")":
        floor -= 1
    # Correct for indexing by 1 (vs 0)
    if floor == -1:
        part2 = i + 1
        break

print("Part 1:", part1)
print("Part 2:", part2)
