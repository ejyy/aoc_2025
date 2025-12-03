part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_03_input.txt", 'r')]

for line in input:
    # Convert each line to a list (keeping as strings for digit concatenation)
    line_nums = list(line)

    # Iterate through each number in the list, building a pair
    row_possibles = []

    for idx, n in enumerate(line_nums):
        for x in range(len(line_nums) - (idx+1)):
            row_possibles.append(int(n + line_nums[idx + (x+1)]))

    # Part1 - Increment by the line's max possible number
    part1 += max(row_possibles)

print("Part 1:", part1)
print("Part 2:", part2)
