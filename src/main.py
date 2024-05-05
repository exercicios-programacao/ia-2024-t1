"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import a_star

if __name__ == "__main__":
    grafo = read_graph("C:/Users/anton/OneDrive/Área de Trabalho/ia-2024-t1-francielli/mapas/small_map.txt")
    vertices_avaliados, custo, caminho = a_star(grafo, 0, 764)
    print(vertices_avaliados, custo, caminho)