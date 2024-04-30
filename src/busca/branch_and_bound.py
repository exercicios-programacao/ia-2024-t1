from graph import get_neighbors

def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    visited = set() # A list with all the already visited nodes.
    stack = [(0, 0, [start])] # Stack to save the new path in process.
    best = [] # List to save the minor cost path found.

    # Loop that tries every new path.
    while stack:
        stack.sort()
        lb, cost, current_path = stack.pop(0)
        node = current_path[-1]

        # Test if the current node is a goal, if a path already got found, and compare two possible paths to get the one with minor cost.
        if node == goal:
            if not best:
                best.append((len(visited), cost, current_path))
            elif best and best[0][1] > cost:
                best[0] = (len(visited), cost, current_path)

        # Algorithm to test every neighbor from the graph.
        if node not in visited:
            visited.add(node)
            neighbors = get_neighbors(graph, node)
            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    if not best or (best and cost + edge_cost < best[0][1]):
                        new_cost = cost + edge_cost
                        new_path = current_path + [neighbor]
                        new_lb = new_cost
                        stack.append((new_lb, new_cost, new_path))

    return best or "Nenhum caminho foi encontrado!"