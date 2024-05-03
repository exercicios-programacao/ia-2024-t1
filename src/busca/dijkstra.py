"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

import sys


def dijkstra(graph, start: int, _goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""

    def min_distance(dist, visited):
        min_value = sys.maxsize
        min_index = -1

        length = len(dist)
        for v in range(length):
            if (visited[v] == 0 and dist[v] <= min_value):
                min_value = dist[v]
                min_index = v

        return min_index

    length = len(graph)

    dist = {}
    visited = {}
    for vertice in graph.get_vertices():
        visited[vertice] = 0
        dist[vertice] = sys.maxsize

    dist[start] = 0

    for _i in range(length - 1):
        u = min_distance(dist, visited)

        visited[u] = 1  # visited

        for v in range(length):
            if (visited[v] == 0 and dist[u] != sys.maxsize):
                dist[v] = dist[u]
