from heapq import heapify, heappush, heappop
from typing import List, Tuple

# Definição da estrutura do grafo
class Graph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.adjacency_list = [[] for _ in range(num_nodes)]
        self.coordinates = {}

    def add_node(self, node: int, latitude: float, longitude: float):
        self.coordinates[node] = (latitude, longitude)

    def add_edge(self, node1: int, node2: int, cost: float):
        self.adjacency_list[node1].append((node2, cost))
        self.adjacency_list[node2].append((node1, cost))

# Função para ler o grafo a partir de um arquivo
def read_graph(filename: str) -> Graph:
    with open(filename, 'r') as file:
        num_nodes = int(file.readline())
        graph = Graph(num_nodes)
        for _ in range(num_nodes):
            node, latitude, longitude = map(float, file.readline().split())
            graph.add_node(int(node), latitude, longitude)
        num_edges = int(file.readline())
        for _ in range(num_edges):
            node1, node2, cost = map(int, file.readline().split())
            graph.add_edge(node1, node2, cost)
    return graph

# Implementação do algoritmo de Dijkstra
def dijkstra(graph: Graph, start: int, goal: int) -> Tuple[int, float, List[int]]:
    num_nodes_explored = 0
    path_length = 0
    path = []

    # Dicionário para manter o custo atual do caminho do nó inicial até cada nó
    distances = {node: float('inf') for node in range(graph.num_nodes)}
    distances[start] = 0

    # Dicionário para manter o nó anterior no caminho mais curto até cada nó
    previous = {}

    # Conjunto de nós não visitados
    unvisited = set(range(graph.num_nodes))

    # Loop principal do algoritmo
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        num_nodes_explored += 1

        if current == goal:
            # Reconstrói o caminho
            while current in previous:
                path.insert(0, current)
                current = previous[current]
            path.insert(0, start)
            path_length = distances[goal]
            return num_nodes_explored, path_length, path

        unvisited.remove(current)

        for neighbor, cost in graph.adjacency_list[current]:
            new_distance = distances[current] + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

    return num_nodes_explored, path_length, path

