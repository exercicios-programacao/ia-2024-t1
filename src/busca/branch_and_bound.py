"""Implementação do algoritmo 'branch and bound'."""

import heapq


def branch_and_bound(graph, start, goal):
    """Busca um caminho entre start e goal usando Branch and Bound."""
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))
    cost_so_far = {start: 0}
    checked = 0

    while frontier:
        current_cost, current_node, path = heapq.heappop(frontier)
        checked += 1

        if current_node == goal:
            return checked, current_cost, path

        for next_node, cost in graph[current_node]['edges'].items():
            new_cost = current_cost + cost

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                new_path = path + [next_node]
                heapq.heappush(frontier, (new_cost, next_node, new_path))

    return float('inf'), float('inf'), []
