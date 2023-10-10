# Define the graph as a dictionary of dictionaries
graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

# Define heuristic values as a dictionary
heuristics = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

# Print the graph
print("Graph:")
for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")

# Print the heuristics
print("\nHeuristics:")
for node, h_value in heuristics.items():
    print(f"{node}: {h_value}")
