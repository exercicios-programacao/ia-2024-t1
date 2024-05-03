"""Implementação de uma estrutura de grafo."""


class Graph:
    """"grafo"""
    def __init__(self, is_direct=False):
        self.vertices = {}
        self.adj = {}
        self.is_direct = is_direct

    def add_vertex(self, vertex, data=None):
        """"adiciona um vertice ao grafo"""
        self.vertices[vertex] = data
        self.adj[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, cost=0.0):
        """"adiciona uma aresta ao grafo"""
        if self.adj[from_vertex] is None:
            self.adj[from_vertex] = {}

        self.adj[from_vertex][to_vertex] = cost

        if not self.is_direct:
            self.adj[to_vertex][from_vertex] = cost

    def __len__(self):
        return len(self.adj)

    def get_vertices(self):
        """"retorna os vertices do grafo"""
        return self.vertices

    def get_neighbors(self, v):
        """"retorna os vizinhos de uma determinada adjacencia do grafo"""
        return self.adj[v]

# ----------------------------------------------------------------


def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""

    graph = Graph()
    with open(filename, "rt", encoding="utf-8") as input_file:
        vertex_count = int(input_file.readline().strip())
        for _ in range(vertex_count):
            index, latitude, longitude = input_file.readline().strip().split()
            graph.add_vertex(int(index), [latitude, longitude])

        edge_count = int(input_file.readline().strip())
        for _ in range(edge_count):
            from_vertex, to_vertex, cost = (
                input_file.readline().strip().split()
            )
            graph.add_edge(int(from_vertex), int(to_vertex), float(cost))

    return graph
