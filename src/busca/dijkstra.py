"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

import heapq

def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""
