part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_01_input.txt", 'r')]

# Define left and right lists
left_list = []
right_list = []

for line in input:
    # Split on whitespace and add left / right numbers to respective lists
    split_line = line.split("   ")
    left_list.append(int(split_line[0]))
    right_list.append(int(split_line[1]))

# Part1 - total distance between left and right lists
left_list.sort()
right_list.sort()

for idx, x in enumerate(left_list):
    part1 += abs(x - right_list[idx])

# Part2 - similarity score
left_dict = {x:left_list.count(x) for x in left_list}
right_dict = {x:right_list.count(x) for x in right_list}

for left_key, left_value in left_dict.items():
    if left_key in right_dict:
        part2 += left_value * (left_key * right_dict[left_key])

print("Part 1:", part1)
print("Part 2:", part2)
