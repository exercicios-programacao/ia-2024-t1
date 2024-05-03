"""Implementação da busca em largura."""

from queue import deque

from ..graph import Graph


def bfs(graph, start, goal):
    """Busca um caminho entre start e goal usando busca em largura."""
    if not isinstance(graph, Graph):
        raise Exception('graph deve ser do tipo Graph')
    if not isinstance(start, int) or start not in graph.nodes:
        raise Exception('start deve ser do tipo int e deve constar em graph.nodes')
    if not isinstance(goal, int) or goal not in graph.nodes:
        raise Exception('goal deve ser do tipo int e deve constar em graph.nodes')

    path, Q, visited, came_from = [goal], deque(), set(), {start: None}
    Q.appendleft(start)

    while Q:
        parent = v = Q.pop()

        if goal == v:
            parent = came_from[goal]
            visited.add(v)
            while parent != start:
                path.append(start)
                parent = came_from[parent]
            path.append(start)
            path, cost = list(reversed(path)), 0
            for itr in range(len(path) - 1):
                cost += graph.cost(path[itr], path[itr + 1])
            return (len(visited), cost, path)

        if v not in visited:
            visited.add(v)
            for u in graph.neighbors(v):
                if u not in visited:
                    came_from[u] = parent
                Q.appendleft(u)
                if u == goal:
                    break
