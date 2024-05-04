"""Funções auxiliares para o projeto"""

import math
from graph import Vertex, AdjacentVertex, Coordinate
from typing import List


def haversine(lat1, lon1, lat2, lon2):
    """Calcula a distância, em metros, entre duas coordenadas GPS."""
    dLat = (lat2 - lat1) * math.pi / 180.0  # pylint: disable=invalid-name
    dLon = (lon2 - lon1) * math.pi / 180.0  # pylint: disable=invalid-name
    # convert to radians
    lat1 = lat1 * math.pi / 180.0
    lat2 = lat2 * math.pi / 180.0
    # apply formulae
    a = (
        pow(math.sin(dLat / 2), 2) +
        pow(math.sin(dLon / 2), 2) *
        math.cos(lat1) * math.cos(lat2)
    )
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return (rad * c)*1000


#
# Não altere este comentário e adicione suas funções ao final do arquivo.
#

def find_neighbor(graph: List[Vertex], node_list: List[int], adjacent_vertex_list: List[AdjacentVertex], goal: int) -> List[List[int]]:
    new_list: List[List[int]] = []
    for vertex in adjacent_vertex_list:
        if not vertex.get_is_visited():
            if goal == vertex.Vertex:
                new_list.append(new_item_of_list(node_list.copy(), vertex.Vertex))
                set_is_visited(graph, node_list[-1], vertex.Vertex)
                return new_list
            else:
                new_list.append(new_item_of_list(node_list.copy(), vertex.Vertex))
                set_is_visited(graph, node_list[-1], vertex.Vertex)
    return new_list


def new_item_of_list(node_list: List[int], new_node: int) -> List[int]:
    node_list.append(new_node)
    return node_list


def get_length_path(graph: List[Vertex], path: List[int]) -> float:
    length_path: float = 0
    for index in range(len(path) - 1):
        latitude1, longitude1 = get_lat_long(graph, path[index])
        latitude2, longitude2 = get_lat_long(graph, path[index + 1])
        length_path += haversine(latitude1, longitude1, latitude2, longitude2)
    return length_path


def get_lat_long(graph: List[Vertex], vertex: int) -> (float, float):
    vertex: Vertex = next(filter(lambda e: vertex == e.Vertex, graph), None)
    return vertex.Coordinate.Latitude, vertex.Coordinate.Longitude


def check_vertex_in_graph(graph: List[Vertex], vertex: int) -> bool:
    find_vertex = next(filter(lambda e: vertex == e.Vertex, graph), None)
    return find_vertex is None


def set_is_visited(graph: List[Vertex], vertex1: int, vertex2: int) -> None:
    vertex_1: Vertex = next(filter(lambda e: e.Vertex == vertex1, graph))
    vertex_2: Vertex = next(filter(lambda e: e.Vertex == vertex2, graph))

    for vertex in vertex_1.AdjacentVertexList:
        if vertex.Vertex == vertex_2.Vertex:
            vertex.set_is_visited(True)

    for vertex in vertex_2.AdjacentVertexList:
        if vertex.Vertex == vertex_1.Vertex:
            vertex.set_is_visited(True)


def reset_is_visited(graph: List[Vertex]) -> None:
    for vertex in graph:
        for adjacent_vertex in vertex.AdjacentVertexList:
            adjacent_vertex.set_is_visited(False)
