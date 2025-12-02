part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

# Separate at every comma (",")
for product_range in input[0].split(","):
    # Separate at every dash ("-")
    split_range = product_range.split("-")

    # Loop through every number (inclusive) within the product range
    for n in range(int(split_range[0]), int(split_range[1]) + 1):
        # Convert number to string to allow splitting
        n = str(n)

        # Part1 - to check if repetitive, split the number in half (as a string)
        n_first_half, n_second_half = n[:len(n)//2], n[len(n)//2:]

        if n_first_half == n_second_half:
            # Increment part1 by the value of the repetitive ID
            part1 += int(n)

        # Part2 - need every permutation of 'fracturing' the number (not just halfing)
        for fracture in range(1, len(n)):
            # Fracture fragment of number (1188511885 -> 1, 11, 118, 1188, 11885 etc)
            fracture_fragment = n[:fracture]

            # Number of repetitions of fragment to rebuild 'n' (1188511885 -> 10, 5, 3, 2, 2 etc)
            number_of_repetitions = (len(n) // fracture)

            # Comparison between rebuild repeted fragment and original number
            if fracture_fragment * number_of_repetitions == n:
                # Increment part2 by the value of the repetitive ID
                part2 += int(n)

                # Break once incremented to prevent double counting
                break

print("Part 1:", part1)
print("Part 2:", part2)
