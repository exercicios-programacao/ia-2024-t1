"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import dfs


if __name__ == "__main__":
    grafo = read_graph("C:\www\ia-2024-t1\mapas\mini_map.txt")

    caminho = dfs(grafo, 3, 7)
    print(caminho)
