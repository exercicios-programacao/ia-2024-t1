"""Implementação da busca em profundidade."""

from ..graph import Graph


def dfs(graph, start, goal):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    if not isinstance(graph, Graph):
        raise Exception('graph deve ser do tipo Graph')
    if not isinstance(start, int) or start not in graph.nodes:
        raise Exception('start deve ser do tipo int e deve constar em graph.nodes')
    if not isinstance(goal, int) or goal not in graph.nodes:
        raise Exception('goal deve ser do tipo int e deve constar em graph.nodes')

    path, visited, came_from = [goal], set(), {start: None}
    S = [start]

    while S:
        parent = v = S.pop()

        if v == goal:
            parent = came_from[goal]
            visited.add(v)
            while parent != start:
                path.append(parent)
                parent = came_from[parent]
            path.append(start)
            path = list(reversed(path))
            cost = 0
            for itr in range(len(path) - 1):
                cost += graph.cost(path[itr], path[itr + 1])
            return (len(visited), cost, path)

        if v not in visited:
            visited.add(v) 
            for u in graph.neighbors(v):
                if u not in visited:
                  came_from[u] = parent
                S.append(u)
                if u == goal:
                  break
