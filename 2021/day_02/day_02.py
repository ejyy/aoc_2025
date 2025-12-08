part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

horizontal = 0
depth = 0
aim = 0

# Part1 - basic logic without aim
for line in input:
    instruction, magnitude = line.split()
    magnitude = int(magnitude)

    if instruction == "forward":
        horizontal += magnitude

    if instruction == "down":
        depth += magnitude

    if instruction == "up":
        depth -= magnitude

part1 = horizontal * depth

# It's just easier to restart here
horizontal = 0
depth = 0
aim = 0

# Part2 - basic logic including aim
for line in input:
    instruction, magnitude = line.split()
    magnitude = int(magnitude)

    if instruction == "forward":
        horizontal += magnitude
        depth += magnitude * aim

    if instruction == "down":
        aim += magnitude

    if instruction == "up":
        aim -= magnitude

part2 = horizontal * depth

print("Part 1:", part1)
print("Part 2:", part2)
