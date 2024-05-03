"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import dfs


if __name__ == "__main__":
    grafo = read_graph("C:/Users/Antonio/Desktop/ia-2024-t1-francielli/mapas/small_map.txt")
    vertices_avaliados, custo, caminho = dfs(grafo, 1, 9)
    print(vertices_avaliados, custo, caminho)