part1 = 0
part2 = 0

# Parse the input file, line by line
input = [list(line.strip().split()) for line in open("day_06_test.txt", 'r')]

import math

# Transpose from rows to columns with zip
nums_transposed = list(zip(*input[:-1]))

# Loop through the symbols
for idx, symbol in enumerate(input[-1]):
    # If symbol '+', perform sum
    if symbol == "+":
        part1 += sum(map(int, nums_transposed[idx]))
    # If symbol '*', multiply out
    if symbol == "*":
        part1 += math.prod(map(int, nums_transposed[idx]))

# Part 2 needs to be completely recalculated, as stripped whitespace in part 1

print("Part 1:", part1)
print("Part 2:", part2)
