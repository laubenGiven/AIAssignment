from queue import PriorityQueue

# Define the graph and heuristics
graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

heuristics = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

# Test the search algorithms
start_node = 'S'
target_node = 'G'

def custom_search(graph, start, target, algorithm, heuristic=None):
    frontier = PriorityQueue()
    frontier.put((0, start, [start]))
    expanded_states = []

    while not frontier.empty():
        _, node, path = frontier.get()

        if node == target:
            return expanded_states, path

        if node not in expanded_states:
            expanded_states.append(node)

            neighbors = graph[node]
            for neighbor, neighbor_cost in sorted(neighbors.items(), key=lambda x: heuristic[x[0]] if heuristic else 0):
                if neighbor not in expanded_states:
                    new_path = path + [neighbor]
                    new_cost = neighbor_cost
                    if algorithm == "UCS" or algorithm == "A*":
                        new_cost += sum(graph[step][neighbor] for step in path if step in graph and neighbor in graph[step])
                    priority = new_cost if algorithm == "UCS" else (new_cost + heuristic[neighbor]) if heuristic else 0
                    frontier.put((priority, neighbor, new_path))

    return None

# Define search algorithms
search_algorithms = {
    "DFS": None,
    "BFS": None,
    "UCS": None,
    "Greedy": heuristics,
    "A*": heuristics
}

# Test each search algorithm
for algorithm, heuristic in search_algorithms.items():
    expanded_states, path = custom_search(graph, start_node, target_node, algorithm, heuristic)
    print(f"{algorithm} Expanded States:", expanded_states)
    print(f"{algorithm} Path:", path)
    print(f"{algorithm} States Not Expanded:", [node for node in graph if node not in expanded_states])
