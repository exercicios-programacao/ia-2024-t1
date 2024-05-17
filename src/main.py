"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import dfs


if __name__ == "__main__":
    grafo = read_graph("C:\\www\\lasalle\\ia-2024-t1\\mapas\\mini_map.txt")
    print(grafo)
    vertices_avaliados, custo, caminho = dfs(grafo, 0, 4)
    print(vertices_avaliados, custo, caminho)
