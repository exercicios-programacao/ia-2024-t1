"""Implementação do algoritmo A* (A-star) para busca do menor caminho em um grafo ponderado não-direcionado."""

from queue import PriorityQueue

from ..utils import haversine, manhattan


def a_star(graph, start, goal):
    """Busca em graph, um caminho entre start e goal usando A*"""
    if not isinstance(graph, graph):
        raise Exception('graph deve ser do tipo Graph')
    if not isinstance(start, int) or start not in graph.nodes:
        raise Exception('start deve ser do tipo int e deve constar em graph.nodes')
    if not isinstance(goal, int) or goal not in graph.nodes:
        raise Exception('goal deve ser do tipo int e deve constar em graph.nodes')
    
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            parent = came_from[current]
            path = [current, parent]
            while parent != start:
                parent = came_from[parent]
                path.append(parent)
            return (len(came_from.keys()), cost_so_far[current], list(reversed(path)))

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # As 2 linhas abaixo não são necessárias para a heurística de Manhattan
                next_lat, next_lon = graph.nodes[next]['lat'], graph.nodes[next]['lon']
                goal_lat, goal_lon = graph.nodes[next]['lat'], graph.nodes[next]['lon']

                priority = new_cost + haversine(next_lat, goal_lat, next_lon, goal_lon) # "manhattan(graph, goal, next)" para calcular com heurística de Manhattan
                frontier.put(next, priority)
                came_from[next] = current
