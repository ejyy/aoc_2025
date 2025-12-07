part1 = 0
part2 = 0

# Parse the input file, line by line
input = [list(line.strip()) for line in open("day_07_test.txt", 'r')]

from collections import deque

# Use a double-ended queue to store all 'current positions'
current_positions = deque()

# Find starting point ("S")
for row_k, row_v in enumerate(input):
    # Process grid column by column
    for column_k, column_v in enumerate(row_v):
        if column_v == "S":
            current_positions.append((row_k, column_k))

while True:
    # A new double_ended queue to store updates
    next_q = deque()

    # Iterate through all current position heads
    while current_positions:
        # Pop from the left of the queue
        x, y = current_positions.popleft()

        # Attempt to move directly downwards
        new_x, new_y = x + 1, y

        # Bounds checking of new position head
        if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
            continue

        # Cell value at new position head
        cell = input[new_x][new_y]

        # If splitter detected
        if cell == "^":
            part1 += 1
            # Left split
            lx, ly = new_x + 1, new_y - 1
            # Bounds checking for left split
            if lx >= 0 or lx < len(input) or ly >= 0 or ly < len(input[0]):
                next_q.append((lx, ly))

            # Right split
            rx, ry = new_x + 1, new_y + 1
            # Bounds checking for right split
            if rx >= 0 or rx < len(input) or ry >= 0 or ry < len(input[0]):
                next_q.append((rx, ry))

        # Unimpeded path
        elif cell == ".":
            next_q.append((new_x, new_y))

    # Break out of loop if all processing done and no new moves
    if not next_q:
        break

    # Update the input grid with the beam paths
    for x, y in next_q:
        input[x][y] = "|"

    # Update current positions with newly created heads
    current_positions = next_q

# Pretty print the grid
for line in input:
    print("".join(line))

# Part1 - sum of beam splits
part1 = sum(input, []).count("|")

print("Part 1:", part1)
print("Part 2:", part2)
