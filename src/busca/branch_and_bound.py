from graph import get_neighbors
from collections import deque

def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    visited = set()  # A set with all the already visited nodes.
    queue = deque([(0, 0, [start])])  # Queue to save the new path in process.
    best = ()  # Tuple to save the minor cost path found.

    # Loop that tries every new path.
    while queue:
        queue = deque(sorted(queue, key=lambda x: x[0]))
        lb, cost, current_path = queue.popleft()
        node = current_path[-1]

        # Test if the current node is a goal, if a path already got found, and compare two possible paths to get the one with minor cost.
        if node == goal:
            if not best or (best and best[1] > cost):
                best = (len(visited), cost, current_path)

        # Algorithm to test every neighbor from the graph.
        if node not in visited:
            visited.add(node)
            neighbors = get_neighbors(graph, node)

            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    if not best or (best and cost + edge_cost < best[1]):
                        new_cost = cost + edge_cost
                        new_path = current_path + [neighbor]
                        new_lb = new_cost
                        queue.append((new_lb, new_cost, new_path))

    return best or "Path not found!"