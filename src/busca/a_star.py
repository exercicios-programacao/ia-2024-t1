"""Implementação do algoritmo A* (A-star) para busca do menor caminho em um grafo ponderado não-direcionado."""

from queue import PriorityQueue


def a_star(graph, start, goal):
    """Busca em graph, um caminho entre start e goal usando A*"""
    if not isinstance(graph, Graph):
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
                priority = new_cost + manhattan(graph, goal, next)
                frontier.put(next, priority)
                came_from[next] = current

def manhattan(graph, a, b):
    """Heurística de Manhattan, usada como estimativa para o valor da aresta que une dois vértices"""
    try:
        a, b = graph.nodes[a], graph.nodes[b]
    except KeyError:
        raise Exception('Não foi possível achar os nodos para os valores a e b - Manhattan - A*')
    return abs(a['lat'] - b['lat']) + abs(a['lon'] - b['lon'])
