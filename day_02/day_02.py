part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

for line in input:
    # Separate at every comma (",")
    for product_range in line.split(","):

        # Separate at every dash ("-")
        split_range = product_range.split("-")

        # Loop through every number (inclusive) within the product range
        for n in range(int(split_range[0]), int(split_range[1]) + 1):

            # To check if repetitive, split the number in half (as a string)
            n = str(n)
            n_first_half, n_second_half = n[:len(n)//2], n[len(n)//2:]

            if n_first_half == n_second_half:
                # Increment part1 by the value of the repetitive ID
                part1 += int(n)

print("Part 1:", part1)
print("Part 2:", part2)
