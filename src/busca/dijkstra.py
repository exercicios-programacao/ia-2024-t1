"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

from heapq import heappush, heappop


def dijkstra(graph, start, goal):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""
    dist = {v: float('inf') for v in graph.keys()}
    prev = {v: None for v in graph.keys()}
    dist[start] = 0
    q = [(0, start)]
    analyzed_nodes = set()
    while q:
        _, u = heappop(q)
        analyzed_nodes.add(u)
        if u == goal:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = prev[current]
            path.reverse()
            return len(analyzed_nodes), dist[goal], path
        for v, w in graph[u]['edges'].items():
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(q, (dist[v], v))
    return len(analyzed_nodes), float('inf'), []
