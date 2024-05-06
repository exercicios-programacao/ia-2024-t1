"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import dfs, bfs, branch_and_bound, a_star, dijkstra

if __name__ == "__main__":
    graph = read_graph("mapas\mini_map.txt")
    print(dfs(graph, 0, 9))
    print(bfs(graph, 0, 9))
    print(branch_and_bound(graph, 0, 9))
    print(a_star(graph, 0, 9))
    print(dijkstra(graph, 0, 9))