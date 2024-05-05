"""Implementação do algoritmo A*."""

from queue import PriorityQueue


def a_star(graph, start, goal):
    """Busca em graph, um caminho entre start e goal usando A*."""
    def heuristic(a, b):
        ax, ay = a['coordinates']
        bx, by = b['coordinates']
        return abs(ax - bx) + abs(ay - by)
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost = {}
    came_from[start] = None
    cost[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next_node, cost in graph[current]['edges'].items():
            new_cost = cost[current] + cost
            if next_node not in cost or new_cost < cost[next_node]:
                cost[next_node] = new_cost
                priority = new_cost + heuristic(graph[start], graph[goal])
                frontier.put(next_node, priority)
                came_from[next_node] = current
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return len(path), cost[goal], path
