from typing import List, Tuple
from collections import deque

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

# Implementação do algoritmo de busca em largura (BFS)
def bfs(graph: Graph, start: int, goal: int) -> Tuple[int, float, List[int]]:
    num_nodes_explored = 0
    path_length = 0
    path = []

    # Estrutura para armazenar os nós visitados
    visited = set()

    # Estrutura para armazenar o caminho percorrido
    parent = {}

    # Fila para BFS
    queue = deque([start])
    visited.add(start)

    # Loop principal do algoritmo
    while queue:
        current = queue.popleft()
        num_nodes_explored += 1

        if current == goal:
            # Reconstrói o caminho
            while current != start:
                path.insert(0, current)
                current = parent[current]
            path.insert(0, start)
            path_length = len(path) - 1  # O comprimento do caminho é o número de nós menos 1
            return num_nodes_explored, path_length, path

        for neighbor, _ in graph.adjacency_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Se o objetivo não for alcançável, retorne um caminho vazio
    return num_nodes_explored, path_length, path
