"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

from heapq import heapify, heappush, heappop

# from util import reverse_path


def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""
