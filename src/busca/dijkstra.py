"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

import heapq import heappush, heappop

from graph import Graph


def dijkstra(graph, start, goal):
    """Busca em graph, um caminho entre start e goal usando Dijkstra"""
    if not isinstance(graph, Graph):
      raise Exception('graph deve ser do tipo Graph')
    if not isinstance(start, int) or start not in graph.nodes:
      raise Exception('start deve ser do tipo int e deve constar em graph.nodes')
    if not isinstance(goal, int) or goal not in graph.nodes:
      raise Exception('goal deve ser do tipo int e deve constar em graph.nodes')

    dist, prev, Q = {}, {}, []
    for v in graph.nodes:
        dist[v] = float('inf')
        prev[v] = None
        if v == start:
            dist[v] = 0
        heappush(Q, (dist[v], v))

    while Q:
        u = heappop(Q)[1]

        if u == goal:
            a, visited, path = u, 0, [u]
            for cost in dist.values():
                visited += 1 if cost != float('inf') else visited
            while a != start:
                path.append(prev[a])
                a = prev[a]
            return (visited, dist[u], list(reversed(path)))

        for v in graph.neighbors(u):
            if v in [tupla[1] for tupla in Q]:
                alt = dist[u] + graph.cost(u, v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
