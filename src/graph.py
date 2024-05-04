"""Implementação de uma estrutura de grafo."""

# import sys


def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    graph = {}
    with open(filename, "rt", encoding="utf-8") as input_file:
        vertex_count = int(input_file.readline().strip())

        for _ in range(vertex_count):  # Counts every vertex
            index, latitude, longitude = input_file.readline().strip().split()

            graph[int(index)] = {'vertex': (float(latitude), float(longitude)), 'edges': []}

        edge_count = int(input_file.readline().strip())

        for _ in range(edge_count):  # Counts every possibility
            from_vertex, to_vertex, cost = (
                input_file.readline().strip().split()
            )

            from_vertex, to_vertex, cost = int(from_vertex), int(to_vertex), float(cost)
            graph[from_vertex]['edges'].append((to_vertex, cost))

    return graph
