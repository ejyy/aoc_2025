part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_03_input.txt", 'r')]

# Function to find the highest joltage for a desired length
def find_highest_joltage(int_list, desired_len):
    # Calculate number of digits can be removed from the line to still build a correct length integer
    num_to_drop = len(int_list) - desired_len

    # Maintain a stack of the 'best' numbers (favouring the leading digit)
    best_stack = []

    # Iterate through the list
    for n in int_list:
        # If still able to drop numbers and next number better the current best on the stack
        while num_to_drop > 0 and best_stack and best_stack[-1] < n:
            # Remove the last item from the stack
            best_stack.pop()
            num_to_drop -= 1
        # Add the better number to the stack
        best_stack.append(n)

    # Concatenate the leading 'desired_len' digits and return as an integer
    return int(''.join(best_stack[:desired_len]))

for line in input:
    # Convert each line to a list (keeping as strings for digit concatenation)
    line_nums = list(line)

    # Part1 - max joltage for 2 batteries
    part1 += find_highest_joltage(line_nums, 2)

    # Part 2 - max joltage for 12 batteries
    part2 += find_highest_joltage(line_nums, 12)

print("Part 1:", part1)
print("Part 2:", part2)
