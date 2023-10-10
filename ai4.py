from queue import PriorityQueue

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


def search(graph, start, target, algorithm, heuristic=None):
    frontier = PriorityQueue()
    frontier.put((0, start, [start]))  # (priority, node, path)
    visited = set()

    while not frontier.empty():
        _, node, path = frontier.get()

        if node == target:
            return path

        if node not in visited:
            visited.add(node)

            neighbors = graph[node]
            for neighbor, neighbor_cost in sorted(neighbors.items(), key=lambda x: heuristic[x[0]] if heuristic else 0):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = neighbor_cost
                    if algorithm == "UCS" or algorithm == "A*":
                        new_cost += sum(graph[step][neighbor] for step in path if step in graph and neighbor in graph[step])  # Calculate total cost
                    priority = new_cost if algorithm == "UCS" else (new_cost + heuristic[neighbor]) if heuristic else 0
                    frontier.put((priority, neighbor, new_path))

    return None

# Perform different searches
dfs_path = search(graph, start_node, target_node, "DFS")
print("DFS Path:", dfs_path)

bfs_path = search(graph, start_node, target_node, "BFS")
print("BFS Path:", bfs_path)

ucs_path = search(graph, start_node, target_node, "UCS")
print("UCS Path:", ucs_path)

greedy_path = search(graph, start_node, target_node, "Greedy", heuristics)
print("Greedy Search Path:", greedy_path)

a_star_path = search(graph, start_node, target_node, "A*", heuristics)
print("A* Search Path:", a_star_path)
