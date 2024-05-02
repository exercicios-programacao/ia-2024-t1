"""Implementação de uma estrutura de grafo."""

import sys


def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    graph = []
    with open(filename, "rt") as input_file:
        vertex_count = int(input_file.readline().strip())
        for _ in range(vertex_count):
            index, latitude, longitude = input_file.readline().strip().split()
            index, latitude, longitude = [ int(index), float(latitude), float(longitude) ]
            graph.append([(latitude, longitude),{}])
            
        edge_count = int(input_file.readline().strip())
        for _ in range(edge_count):
            from_vertex, to_vertex, cost = (
                input_file.readline().strip().split()
            )
            from_vertex, to_vertex, cost = [ int(from_vertex), int(to_vertex), float(cost) ]
            graph[from_vertex][1][to_vertex] = cost
            graph[to_vertex][1][from_vertex] = cost

    return graph
