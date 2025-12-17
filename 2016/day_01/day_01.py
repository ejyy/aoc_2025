part1 = 0
part2 = None

# Parse the input file, line by line
input = [line.strip() for line in open("day_01_input.txt", 'r')][0].split(",")

# Direction reference (N, E, S, W)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_index = 0

# Current starting position (x, y)
x, y = 0, 0

# Set of visited locations
visited = {(0, 0)}

for instruction in input:
    # Split the instruction string to obtain turn and magnitude
    instruction = instruction.strip()
    turn = instruction[0]
    magnitude = int(instruction[1:])

    # Work through direction index based on turn direction
    if turn == "R":
        direction_index += 1
    elif turn == "L":
        direction_index -= 1

    # Direction from current position based on index lookup to directions
    dx, dy = directions[direction_index % len(directions)]

    # Apply change to current position based on magnitude (one-by-one for part 2)
    for _ in range(magnitude):
        x += dx
        y += dy

        if (x, y) in visited and part2 is None:
            part2 = abs(x) + abs(y)
        visited.add((x, y))

# Part1 - total absolute distance in x and y axes
part1 = abs(x) + abs(y)

print("Part 1:", part1)
print("Part 2:", part2)
