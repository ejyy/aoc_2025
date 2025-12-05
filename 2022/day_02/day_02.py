part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

# Player key, Opponent value [win, draw, loss]
player_wins = {
  "X": ["C", "A", "B"], # Rock defeats Scissors
  "Y": ["A", "B", "C"], # Paper defeats Rock
  "Z": ["B", "C", "A"],  # Scissors defeats Paper
}

for line in input:
    # Split the input to derive opponent and player moves
    opponent, player = line.split(" ")

    # Lookup player move by index, adding one to obtain the shape score
    shape_score = list(player_wins).index(player) + 1

    # Lookup player move to find move against opponent for win / draw / loss
    win, draw, loss = player_wins[player]
    result_score = 0

    # Increment the result score by the correct ammount based on result
    if opponent == win:
        result_score += 6
    if opponent == draw:
        result_score += 3

    # Part1 - total score according to strategy guide
    part1 += (shape_score + result_score)

print("Part 1:", part1)
print("Part 2:", part2)
