"""Implementação do algoritmo A*."""
from queue import PriorityQueue
from util import haversine


def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    const_so_far = {}
    came_from[start] = None
    const_so_far[start] = 0
    count_nodes = 0
    while not frontier.empty():
        _, current = frontier.get()
        count_nodes += 1
        if current == goal:
            predecessor = came_from[current]
            path = [current]
            while predecessor is not None:
                path.append(predecessor)
                predecessor = came_from[predecessor]
            path.reverse()
            break

        for next_node, next_node_cost in graph[current][1].items():
            new_cost = const_so_far[current] + next_node_cost

            if (
                next_node not in const_so_far or
                new_cost < const_so_far[next_node]
            ):
                const_so_far[next_node] = new_cost
                priority = new_cost + haversine(
                    graph[goal][0][0],
                    graph[goal][0][1],
                    graph[next_node][0][0],
                    graph[next_node][0][1]
                )
                frontier.put((priority, next_node))
                came_from[next_node] = current
    return (count_nodes, const_so_far[goal], path)
