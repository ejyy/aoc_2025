# /// script
# dependencies = ['networkx']
# ///

part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_11_input.txt", 'r')]

# Use networkx to construct directed graph
import networkx as nx

G = nx.DiGraph()

for line in input:
    # Split to obtain the source and destination
    line_split = line.split(":")
    source = line_split[0]
    destinations = line_split[1].split()
    # Iterate through all destinations and add to the graph
    for destination in destinations:
        G.add_edge(source, destination)

# Networkx to compute all paths from you -> out
all_paths_part1 = nx.all_simple_paths(G, source="you", target="out")
part1 = sum(1 for _ in all_paths_part1)

# Networkx to compute all paths from svr -> out
all_paths_part2 = nx.all_simple_paths(G, source="svr", target="out")

for path in all_paths_part2:
    # Check if path contains both dac and fft
    if all(node in path for node in ["dac", "fft"]):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
