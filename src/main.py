"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import dfs


if __name__ == "__main__":
    grafo = read_graph("C:\www\lasalle\ia-2024-t1\mapas\mini_map.txt")

    caminho = dfs(grafo, 0, 6)
    print(caminho)
