"""Implementação da busca em profundidade."""
from collections import deque
from graph import get_neighbors

CONST_NEIGHBOR_VERTEX_INDEX = 0
CONST_WEIGHT_INDEX = 1
LENGTH = 0.0
PATH = []


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    queue = deque()
    visited = []
    queue.appendleft((start, 0))  # starts with 0 because you are in the vertex
    while queue:
        edge = queue.pop()
        if goal == edge[CONST_NEIGHBOR_VERTEX_INDEX]:
            process(edge)
            return len(visited), LENGTH, PATH
        if edge[CONST_NEIGHBOR_VERTEX_INDEX] not in visited:
            process(edge)
            visited.append(edge[CONST_NEIGHBOR_VERTEX_INDEX])
            for new_edge in get_neighbors(graph, edge[CONST_NEIGHBOR_VERTEX_INDEX]):
                queue.appendleft(new_edge)


def process(edge):
    """Para cada iteração do codigo processa o path e o lenght"""
    global LENGTH, PATH
    PATH.append(edge[CONST_NEIGHBOR_VERTEX_INDEX])
    LENGTH += edge[CONST_WEIGHT_INDEX]
