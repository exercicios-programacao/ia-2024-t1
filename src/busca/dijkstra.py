"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""
from typing import List

from graph import AdjacentVertex
from util import get_length_path


def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    best_so_far: float = float("inf")
    queue = [[[start], 0]]
    best_path = []
    number_graph_nodes_analyzed: int = 0

    while len(queue) > 0:
        vertex_list_to_analyze = queue.pop(0)
        adjacent_vertex_list: List[AdjacentVertex] = next(
            filter(lambda e: e.Vertex == vertex_list_to_analyze[0][-1], graph), None).AdjacentVertexList
        new_items_of_queue = dijkstra_find_neighbor(adjacent_vertex_list, vertex_list_to_analyze, best_so_far)

        for index, (path, cost) in enumerate(new_items_of_queue):
            number_graph_nodes_analyzed += 1
            if path[-1] == goal and cost < best_so_far:
                best_path = path
                best_so_far = cost
                del new_items_of_queue[index]

        queue.extend(new_items_of_queue)
    print("FINAL: ", best_path, best_so_far)
    length_found_path = get_length_path(graph, best_path)
    return number_graph_nodes_analyzed, length_found_path, best_path


def dijkstra_find_neighbor(adjacent_vertex_list: List[AdjacentVertex], vertex_list_to_analyze, best_so_far: float):
    new_list = []
    for vertex in adjacent_vertex_list:
        if vertex.Vertex not in vertex_list_to_analyze[0]:
            new_vertex_in_list = dijkstra_new_item_of_list(vertex_list_to_analyze[0].copy(), vertex_list_to_analyze[1], vertex, best_so_far)
            if len(new_vertex_in_list) > 0:
                new_list.append(new_vertex_in_list)
    return new_list


def dijkstra_new_item_of_list(node_list: List[int], cost: float, new_vertex: AdjacentVertex, best_so_far: float):
    cost += new_vertex.Cost
    if cost < best_so_far:
        node_list.append(new_vertex.Vertex)
        return [node_list, cost]
    else:
        return []


"""Busca em graph, um caminho entre start e goal usando Dijkstra."""
