part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_01_input.txt", 'r')]

# Equation to calculate fuel for given mass
def calc_fuel(mass):
    return mass // 3 - 2

for line in input:
    # Convert mass to an integer
    mass = int(line)

    # Part1 - sum the fuel required (not accounting for the fuel itself)
    fuel_required = calc_fuel(mass)
    part1 += fuel_required

    # Part2 - sum the fuel required (including the fuel's fuel)
    total = 0
    fuel = calc_fuel(mass)

    while fuel > 0:
        total += fuel
        fuel = calc_fuel(fuel)

    part2 += total

print("Part 1:", part1)
print("Part 2:", part2)
