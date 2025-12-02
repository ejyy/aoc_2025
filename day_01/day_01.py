part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_01_input.txt", 'r')]

# The dial's starting position is 50
current_position = 50

for line in input:
    # Extract the direction (ie. L50 -> L)
    direction = str(line[0])

    # Extract the magnitude (ie. L50 -> 50)
    magnitude = int(line[1:])

    # Simulate the dial turning, one step at a time
    for _ in range(magnitude):
        # Right is positive, left is negative
        if direction == "R":
            # Modulo function (remainder of division) for new dial index
            current_position = (current_position + 1) % 100
        else:
            current_position = (current_position - 1) % 100

        # Part2 - number of times it 'touches' zero
        if current_position == 0:
            part2 += 1

    # Part1 - number of times it 'stops' on zero (after each instruction)
    if current_position == 0:
        part1 += 1

print("Part 1:", part1)
print("Part 2:", part2)
