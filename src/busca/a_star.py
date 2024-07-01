"""Implementação do algoritmo A*."""
from queue import PriorityQueue

from util import haversine

def a_star(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    path = [start]
    checked = 0

    while not frontier.empty():
        current = frontier.get()[1]
        checked += 1

        if current == goal:
            while came_from[current] != None:
                path.insert(1, current)
                current = came_from[current]
                
            return checked, cost_so_far[goal], path

        for next in graph[current][1].keys():
            new_cost = cost_so_far[current] + graph[current][1][next]

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + haversine(graph[goal][0][0], graph[goal][0][1], graph[next][0][0], graph[next][0][1])

                frontier.put((priority, next))

                came_from[next] = current