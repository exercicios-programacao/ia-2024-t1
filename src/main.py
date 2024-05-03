"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import a_star


if __name__ == "__main__":
    grafo = read_graph("C:\www\lasalle\ia-2024-t1\mapas\mini_map.txt")

    vertices_avaliados, custo, caminho = a_star(grafo, 0, 7)
    print(vertices_avaliados, custo, caminho)
