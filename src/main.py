"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import dfs
from busca import bfs

if __name__ == "__main__":
    grafo = read_graph("../mapas/mini_map.txt")
    caminho_dfs = dfs(grafo, 0, 9)
    caminho_bfs = bfs(grafo, 0, 9)

    print(caminho_dfs)
    print(caminho_bfs)
