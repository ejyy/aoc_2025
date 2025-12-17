part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_03_input.txt", 'r')]

for line in input:
    sides = sorted(map(int, line.split()))

    if sides[0] + sides[1] > sides[2]:
        part1 += 1

print("Part 1:", part1)
print("Part 2:", part2)
