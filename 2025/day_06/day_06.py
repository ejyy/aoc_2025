part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip().split() for line in open("day_06_test.txt", 'r')]

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

from collections import defaultdict

# Loop through the symbols
for idx, symbol in enumerate(input[-1]):
    # Extract total number of digits of the largest number
    max_len = len(str(max(list(input_np[idx]))))

    padded_nums = [str(num).rjust(max_len) for num in list(input_np[idx])]

    print(padded_nums)

    # position_by_index = defaultdict(list)

    # for i in range(max_len - 1, -1, -1):
    #     for n in list(input_np[idx]):
    #         n = str(n)[::-1]
    #         if i < len(n):
    #             position_by_index[i].append(n[i])

    # s = sorted(position_by_index.items())

    # sum_nums = []

    # for k,v in s:
    #     merged_num = "".join(v)
    #     sum_nums.append(int(merged_num))

    # # If symbol '+', perform sum
    # if symbol == "+":
    #     part2 += sum(list(sum_nums))
    # multiply = 1
    # # If symbol '*', multiply out
    # if symbol == "*":
    #     for n in list(sum_nums):
    #         multiply *= n
    #     part2 += multiply

print("Part 1:", part1)
print("Part 2:", part2)
