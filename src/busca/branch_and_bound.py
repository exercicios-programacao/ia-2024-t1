"""Implementação do algoritmo 'branch and bound'."""

import heapq

def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando Branch and Bound."""
    queue = [(0, start, [start])]
    dist = {index: float('inf') for index, _ in enumerate(graph)}
    while queue:
        vertex_dist, vertex, path = heapq.heappop(queue)
        if vertex == goal:
            return len(path), vertex_dist, path
        for nbor_vertex, weight in graph[vertex][1].items():
            new_dist = vertex_dist + weight
            if new_dist < dist[nbor_vertex]:
                dist[nbor_vertex] = new_dist
                heapq.heappush(queue, (new_dist, nbor_vertex, path + [nbor_vertex]))
    return float('inf'), None, []