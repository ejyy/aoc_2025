part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip().split() for line in open("day_06_input.txt", 'r')]

import numpy as np
import operator

# Process all integers (excluding symbols) into numpy array
input_np = np.asarray(input[:-1], dtype='int64')

# Transpose the numpy
input_np = np.transpose(input_np)

# Loop through the symbols
for idx, symbol in enumerate(input[-1]):
    # If symbol '+', perform sum
    if symbol == "+":
        part1 += sum(list(input_np[idx]))
    multiply = 1
    # If symbol '*', multiply out
    if symbol == "*":
        for n in list(input_np[idx]):
            multiply *= n
        part1 += multiply

print("Part 1:", part1)
print("Part 2:", part2)
