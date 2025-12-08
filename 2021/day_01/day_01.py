part1 = 0
part2 = 0

# Parse the input file, line by line (as integers)
input = [int(line.strip()) for line in open("day_01_input.txt", 'r')]

# Part1 - individual
for idx, line in enumerate(input):
    # Ignore the first entry
    if idx == 0:
        continue

    # Compare current line with previous
    if line > input[idx - 1]:
        part1 += 1

sliding = [sum(input[i:i+3]) for i in range(len(input)-3+1)]

# Part2 - 3-sliding window
for idx, line in enumerate(sliding):
    # Ignore the first entry
    if idx == 0:
        continue

    # Compare current line with previous
    if line > sliding[idx - 1]:
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
