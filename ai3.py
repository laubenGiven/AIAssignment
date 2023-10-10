def search(graph, start, target, heuristic=None):
    # Initialize the data structure based on whether heuristic is provided
    if heuristic:
        priority_queue = [(heuristic[start], 0, start, [start])]
    else:
        queue = [(start, [start])]

    while True:
        if heuristic:
            if not priority_queue:
                return None  # No path found
            _, cost, node, path = priority_queue.pop(0)
        else:
            if not queue:
                return None  # No path found
            node, path = queue.pop(0)
            cost = 0  # Initialize cost to 0 for non-cost-based searches

        if node == target:
            return path

        neighbors = graph[node]
        for neighbor, neighbor_cost in sorted(neighbors.items(), key=lambda x: heuristic[x[0]] if heuristic else 0):
            if neighbor not in path:
                new_path = path + [neighbor]
                new_cost = cost + neighbor_cost
                if heuristic:
                    priority_queue.append((heuristic[neighbor] + new_cost, new_cost, neighbor, new_path))
                    priority_queue.sort(key=lambda x: x[0])
                else:
                    queue.append((neighbor, new_path))

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

start_node = 'S'
target_node = 'G'
# Perform different searches
dfs_path = search(graph, start_node, target_node)
print("DFS Path:", dfs_path)

bfs_path = search(graph, start_node, target_node)
print("BFS Path:", bfs_path)

ucs_path = search(graph, start_node, target_node)
print("UCS Path:", ucs_path)

greedy_path = search(graph, start_node, target_node, heuristics)
print("Greedy Search Path:", greedy_path)

a_star_path = search(graph, start_node, target_node, heuristics)
print("A* Search Path:", a_star_path)
