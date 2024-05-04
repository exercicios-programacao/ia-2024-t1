"""Implementação da busca em profundidade."""

from collections import deque


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    if goal not in graph:
        raise ValueError("Goal doesn't exist in this graph")

    visited = set()
    queue = deque([(start, [start], 0.0)])

    while queue:
        current_node, path, cost = queue.popleft()

        if current_node == goal:
            return len(path), cost, path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]['edges']:
                if neighbor not in visited:
                    total_cost = cost + 1
                    queue.append((neighbor, path + [neighbor], total_cost))

    raise ValueError("Goal node is not reachable from the start node")
