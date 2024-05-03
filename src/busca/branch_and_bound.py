"""Implementação do algoritmo 'branch and bound'."""

from queue import deque

from ..graph import Graph


def branch_and_bound(graph, start, goal):
    """Busca um caminho entre start e goal usando Branch and Bound."""
    if not isinstance(graph, Graph):
        raise Exception('graph deve ser do tipo Graph')
    if not isinstance(start, int) or start not in graph.nodes:
        raise Exception('start deve ser do tipo int e deve constar em graph.nodes')
    if not isinstance(goal, int) or goal not in graph.nodes:
        raise Exception('goal deve ser do tipo int e deve constar em graph.nodes')

    best_so_far = (None, float('inf'))
    Q = deque()
    Q.appendleft(start)

    while Q:
        v = Q.pop()

        if goal == v:
            new_path, candidate = 
            path, limit = best_so_far
