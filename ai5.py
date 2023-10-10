from queue import PriorityQueue

# Define the custom graph and heuristics
custom_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

custom_heuristics = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

# Define a common search function
def custom_search(graph, start, target, algorithm, heuristic=None):
    frontier = PriorityQueue()
    frontier.put((0, start, [start]))  # (priority, node, path)
    visited_nodes = set()
    expanded_states = []

    while not frontier.empty():
        _, node, path = frontier.get()

        if node == target:
            return expanded_states, path

        if node not in visited_nodes:
            visited_nodes.add(node)
            expanded_states.append(node)

            neighbors = graph[node]
            for neighbor, neighbor_cost in sorted(neighbors.items(), key=lambda x: heuristic[x[0]] if heuristic else 0):
                if neighbor not in visited_nodes:
                    new_path = path + [neighbor]
                    new_cost = neighbor_cost
                    if algorithm == "UCS" or algorithm == "A*":
                        new_cost += sum(graph[step][neighbor] for step in path if step in graph and neighbor in graph[step])
                    priority = new_cost if algorithm == "UCS" else (new_cost + heuristic[neighbor]) if heuristic else 0
                    frontier.put((priority, neighbor, new_path))

    return None

# Test the custom search algorithms
custom_start_node = 'S'
custom_target_node = 'G'

# Depth-First Search
expanded_states_dfs, dfs_path = custom_search(custom_graph, custom_start_node, custom_target_node, "DFS")
print("DFS Expanded States:", expanded_states_dfs)
print("DFS Path:", dfs_path)
print("DFS States Not Expanded:", [node for node in custom_graph if node not in expanded_states_dfs])

# Breadth-First Search
expanded_states_bfs, bfs_path = custom_search(custom_graph, custom_start_node, custom_target_node, "BFS")
print("\nBFS Expanded States:", expanded_states_bfs)
print("BFS Path:", bfs_path)
print("BFS States Not Expanded:", [node for node in custom_graph if node not in expanded_states_bfs])

# Uniform Cost Search
expanded_states_ucs, ucs_path = custom_search(custom_graph, custom_start_node, custom_target_node, "UCS")
print("\nUCS Expanded States:", expanded_states_ucs)
print("UCS Path:", ucs_path)
print("UCS States Not Expanded:", [node for node in custom_graph if node not in expanded_states_ucs])

# Greedy Search
expanded_states_greedy, greedy_path = custom_search(custom_graph, custom_start_node, custom_target_node, "Greedy", custom_heuristics)
print("\nGreedy Search Expanded States:", expanded_states_greedy)
print("Greedy Search Path:", greedy_path)
print("Greedy Search States Not Expanded:", [node for node in custom_graph if node not in expanded_states_greedy])

# A* Search
expanded_states_a_star, a_star_path = custom_search(custom_graph, custom_start_node, custom_target_node, "A*", custom_heuristics)
print("\nA* Search Expanded States:", expanded_states_a_star)
print("A* Search Path:", a_star_path)
print("A* Search States Not Expanded:", [node for node in custom_graph if node not in expanded_states_a_star])
