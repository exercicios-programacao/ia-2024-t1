from graph import read_graph
from busca import dfs
from busca import bfs
from busca import dijkstra
from busca import a_star
from busca import branch_and_bound


if __name__ == "__main__":
    graph = read_graph('mapas/mini_map.txt')
    #print(graph)
    print(branch_and_bound(graph, 0, 7))
