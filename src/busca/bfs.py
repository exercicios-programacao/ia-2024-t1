"""Implementação da busca em profundidade."""

from queue import deque as Queue

# from util import reverse_path


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
