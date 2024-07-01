"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""
from heapq import heapify, heappush, heappop

def dijkstra(graph, start, goal):
    return

'''
    if (start in graph and goal in graph):

        distance = {v: float('inf') for v in graph.keys()}
        previous = {v: None for v in graph.keys()}
        distance[start] = 0
        priority_q = [(0, start)]
        nodesAnalized = 0
        path = []

        while priority_q:
            current_distance, u = heappop(priority_q)
            nodesAnalized = nodesAnalized + 1

            if u == goal:
                current_node = goal
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous[current_node]
                path.reverse()
                return (nodesAnalized, distance[goal], path)
            
            for i in graph[u]:
                if type(i) is dict:
                    for vertex, cost in i.items():
                        alternative_path = distance[u] + cost
                        
                    if alternative_path < distance[vertex]:
                        distance[vertex] = alternative_path
                        previous[vertex] = u
                        heappush(priority_q, (distance[vertex], vertex))

    else:
        raise Exception('Vértice não encontrado no grafo')'''
