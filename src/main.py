from graph import read_graph
from busca import a_star


if __name__ == "__main__":
    grafo = read_graph("mini_map.txt")
    vertices_avaliados, custo, caminho = a_star(grafo, 1, 100)
    print(vertices_avaliados, custo, caminho)