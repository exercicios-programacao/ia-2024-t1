"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import dijkstra

if __name__ == "__main__":
    graph = read_graph('mapas/mini_map.txt')
    print(graph)
    print(dijkstra(graph, 0, 9))
