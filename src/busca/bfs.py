# pylint:disable=duplicate-code
"""Implementação da busca em largura."""


class Queue:
    """implementacao de fila"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """adiciona um elemento na fila"""
        self.items.append(item)

    def dequeue(self):
        """remove um elemento da fila"""
        return self.items.pop(0)

    def is_empty(self):
        """retorna se a pilha esta vazia ou nao"""
        return len(self.items) == 0

    def purge(self):
        """limpa a fila"""
        self.items = []


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    count_visited = 0
    total_length = 0.0
    path = []

    queue = Queue()
    queue.enqueue(start)

    visited = {}
    for vertice in graph.get_vertices():
        visited[vertice] = 0

    visited[start] = 1  # visited

    while not queue.is_empty():
        u = queue.dequeue()

        path.append(u)

        if u == goal:
            return (count_visited, total_length, path)

        count_visited = count_visited + 1

        neighbors = graph.get_neighbors(u)

        for neighbor in neighbors.keys():
            if visited[neighbor] == 0:

                if neighbor == goal:
                    path.append(neighbor)

                    return (count_visited, total_length, path)

                visited[neighbor] = 1  # visited
                queue.enqueue(neighbor)

    return None
