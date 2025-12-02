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

    # Left is negative, right is positive
    magnitude = -magnitude if direction == "L" else magnitude

    # Difference based on instruction magnitude relative to current position
    total_delta = current_position + magnitude

    # Modulo function (remainder of division) for new dial index
    current_position = total_delta % 100

    # Part1 - if 'rests' on 0 after the instruction, increment part1
    if current_position == 0:
        part1 += 1

    # Part2 - number of 'revolutions' around the dial face
    part2 += abs(total_delta // 100)
    # TODO: Need to catch some edge cases here, likely due to stopping not crossing 0

print("Part 1:", part1)
print("Part 2:", part2)
