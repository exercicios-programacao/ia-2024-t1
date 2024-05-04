"""Implementação da busca em profundidade."""

# from util import reverse_path


def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    if goal not in graph:
        raise ValueError("Goal node does not exist in the graph")

    visited = set()
    stack = [(start, [start], 0.0)]

    while stack:
        current_node, path = stack.pop()

        if current_node == goal:
            return len(path), float(len(path) -1), path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]['edges']:
                if neighbor[0] not in visited:
                    stack.append((neighbor[0], path + [neighbor[0]], 1))

    raise ValueError("Goal node is not reachable from the start node")
