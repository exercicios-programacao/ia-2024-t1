
"""Implementação de uma estrutura de grafo."""

from typing import List


class Coordinate:
    def __init__(self, latitude: float, longitude: float):
        self.Latitude: float = latitude
        self.Longitude: float = longitude


class AdjacentVertex:
    def __init__(self, vertex: int, cost: float, is_visited: bool):
        self.Vertex = vertex
        self.Cost = cost
        self.IsVisited = is_visited

    def set_is_visited(self, is_visited: bool):
        self.IsVisited = is_visited

    def get_is_visited(self):
        return self.IsVisited


class Vertex:
    def __init__(self, vertex: int, coordinate: Coordinate):
        self.Vertex: int = vertex
        self.Coordinate: Coordinate = coordinate
        self.AdjacentVertexList: List[AdjacentVertex] = []

    def set_adjacent_vertex(self, adjacent_vertex: AdjacentVertex):
        self.AdjacentVertexList.append(adjacent_vertex)


def read_graph(filename: str) -> List[Vertex]:
    graph_dict: {int: int} = {}  # Dicionário para mapear vértices para índices na lista graph_list
    graph: List[Vertex] = []
    with open(filename, "rt") as input_file:
        vertex_count: int = int(input_file.readline().strip())
        for _ in range(vertex_count):
            line: List[str] = input_file.readline().strip().split()

            vertex_node: int = int(line[0])
            latitude: float = float(line[1])
            longitude: float = float(line[2])

            coordinate: Coordinate = Coordinate(latitude, longitude)
            vertex: Vertex = Vertex(vertex_node, coordinate)
            graph.append(vertex)

            graph_dict[vertex_node] = len(graph) - 1  # Mapear o vértice para o índice na lista

        edge_count: int = int(input_file.readline().strip())
        for _ in range(edge_count):
            line: List[str] = input_file.readline().strip().split()

            from_vertex: int = int(line[0])
            to_vertex: int = int(line[1])
            cost: float = float(line[2])

            from_index: int = graph_dict[from_vertex]
            to_index: int = graph_dict[to_vertex]

            vertex_exists: bool = False
            for adjacent_vertex in graph[from_index].AdjacentVertexList:
                if adjacent_vertex.Vertex == to_vertex:
                    vertex_exists = True

            if not vertex_exists:
                graph[from_index].set_adjacent_vertex(AdjacentVertex(to_vertex, cost, False))

            vertex_exists = False
            for adjacent_vertex in graph[to_index].AdjacentVertexList:
                if adjacent_vertex.Vertex == from_vertex:
                    vertex_exists = True

            if not vertex_exists:
                graph[to_index].set_adjacent_vertex(AdjacentVertex(from_vertex, cost, False))
    return graph
