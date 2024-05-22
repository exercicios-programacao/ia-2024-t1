"""Implementação do algoritmo de dfs."""

from util import mountpath


def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    try:
        assert graph[start]
        assert graph[goal]
    except IndexError:
        print("Node doesn't exist")
        return None
    stack = [(start, None)]
    visited_nodes = {}
    count_nodes = 0
    while stack:
        current, predecessor = stack.pop()
        if goal == current:
            path, total_cost = mountpath(
                visited_nodes,
                current,
                predecessor,
                graph
            )

            break

        if current not in visited_nodes:
            count_nodes += 1
            visited_nodes[current] = predecessor
            for neighbor, _ in graph[current][1].items():
                if neighbor not in visited_nodes:
                    stack.append((neighbor, current))

    return (count_nodes, total_cost, path)
