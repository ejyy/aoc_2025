part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

for line in input:
    # Extract L, W, H from input
    l, w, h = map(int, line.split("x"))

    # Part1 - sum required paper plus additional for smallest side
    part1 += sum([2*l*w, 2*w*h, 2*h*l, min(l*w, w*h, h*l)])

    # Part2 - sum ribbon length
    sides = sorted([l, w, h])
    # Sort by smallest sides
    rib_len = 2*sides[0] + 2*sides[1] + (l*w*h)
    part2 += rib_len

print("Part 1:", part1)
print("Part 2:", part2)
