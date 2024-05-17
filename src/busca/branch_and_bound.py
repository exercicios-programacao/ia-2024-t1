"""Implementação do algoritmo de branch and bound."""

from util import mountpath


def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando branch and bound."""
    try:
        assert graph[start]
        assert graph[goal]
    except RuntimeError:
        print("Node doesn't exist")
        return None

    queue = [(start, None)]
    visited_nodes = {}
    best_path = None
    best_cost = float('inf')
    count_nodes = 0

    while queue:
        current_node, predecessor = queue.pop(0)

        if goal == current_node:

            path, total_cost = mountpath(
                visited_nodes,
                current_node,
                predecessor,
                graph
            )

            if total_cost < best_cost:
                best_path = path
                best_cost = total_cost
            continue

        if current_node not in visited_nodes:
            count_nodes += 1
            visited_nodes[current_node] = predecessor

            for neighbor, cost in graph[current_node][1].items():
                if neighbor not in visited_nodes and cost < best_cost:
                    queue.append((neighbor, current_node))

    if best_path is not None:
        return (count_nodes, best_cost, best_path)

    return None
