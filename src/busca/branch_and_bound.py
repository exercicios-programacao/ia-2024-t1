from typing import List, Tuple

# Definição da estrutura do grafo
class Graph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.adjacency_list = [[] for _ in range(num_nodes)]

    def add_edge(self, node1: int, node2: int, cost: float):
        self.adjacency_list[node1].append((node2, cost))
        self.adjacency_list[node2].append((node1, cost))

# Função para ler o grafo a partir de um arquivo
def read_graph(filename: str) -> Graph:
    with open(filename, 'r') as file:
        num_nodes = int(file.readline())
        graph = Graph(num_nodes)
        for _ in range(num_nodes):
            node, _, _ = map(int, file.readline().split())
        num_edges = int(file.readline())
        for _ in range(num_edges):
            node1, node2, cost = map(int, file.readline().split())
            graph.add_edge(node1, node2, cost)
    return graph

def branch_and_bound(graph: Graph, start: int, goal: int) -> Tuple[int, float, List[int]]:
    num_nodes_explored = 0
    shortest_path_length = float('inf')
    shortest_path = []

    def branch_and_bound_helper(current_node: int, path: List[int], path_length: float):
        nonlocal num_nodes_explored, shortest_path_length, shortest_path
        num_nodes_explored += 1

        if current_node == goal:
            if path_length < shortest_path_length:
                shortest_path_length = path_length
                shortest_path = path.copy()
            return

        for neighbor, cost in graph.adjacency_list[current_node]:
            if neighbor not in path:
                if path_length + cost < shortest_path_length:
                    branch_and_bound_helper(neighbor, path + [neighbor], path_length + cost)

    branch_and_bound_helper(start, [start], 0)

    return num_nodes_explored, shortest_path_length, shortest_path
