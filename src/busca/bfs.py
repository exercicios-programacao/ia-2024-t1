"""Implementação da busca em profundidade."""
from collections import deque
from src.graph import get_neighbors

CONST_NEIGHBOR_VERTEX_INDEX = 0
CONST_WEIGHT_INDEX = 1
number_of_visited = 0
length = 0.0
path = []


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    queue = deque()
    visited = []
    queue.appendleft((start, 0))  # starts with 0 because you are in the vertex

    while queue:
        edge = queue.pop()
        if goal == edge[CONST_NEIGHBOR_VERTEX_INDEX]:
            process(edge)
            return number_of_visited, length, path
        if edge not in visited:
            process(edge)
            visited.append(edge[CONST_NEIGHBOR_VERTEX_INDEX])
            for new_edge in get_neighbors(graph, edge[CONST_NEIGHBOR_VERTEX_INDEX]):
                queue.appendleft(new_edge)


def process(edge):
    global number_of_visited, length, path
    number_of_visited += 1
    path.append(edge[CONST_NEIGHBOR_VERTEX_INDEX])
    length += edge[CONST_WEIGHT_INDEX]
