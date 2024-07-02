"""Implementação do algoritmo A*."""

import heapq
from util import haversine


def a_star(graph, start, goal):
    """Busca em graph, um caminho entre start e goal usando A*."""
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    path = [start]
    checked = 0

    while frontier:
        current = heapq.heappop(frontier)[1]
        checked += 1

        if current == goal:
            while came_from[current] is not None:
                path.insert(1, current)
                current = came_from[current]
            return checked, cost_so_far[goal], path

        for next_node in graph[current]['edges'].keys():
            new_cost = cost_so_far[current] + graph[current]['edges'][next_node]

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + haversine(
                    graph[goal]['coordinates'][0], graph[goal]['coordinates'][1],
                    graph[next_node]['coordinates'][0], graph[next_node]['coordinates'][1]
                )
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current
    return float('inf'), float('inf'), []
