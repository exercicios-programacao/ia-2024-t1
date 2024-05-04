"""Utilize este arquivo para depurar seus algoritmos."""

from typing import List
from graph import read_graph, Vertex
from busca import dfs, bfs, branch_and_bound, a_star, dijkstra
from util import reset_is_visited
# from util import reset_is_visited

if __name__ == "__main__":
    graph: List[Vertex] = read_graph("../mapas/mini_map.txt")

    # region DIJKSTRA
    number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal = dijkstra(graph, 0, 6)
    
    print("Dijkstra")
    print("Quantidade de nós analizados: " + str(number_graph_nodes_analyzed))
    print("Tamanho do caminho encontrado: " + str(length_found_path))
    print("Caminho entre o nó inicial e o nó final: " + str(path_between_start_and_goal))
    # endregion DIJKSTRA
    
    reset_is_visited(graph)

    # region BRANCH AND BOUND
    number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal = branch_and_bound(graph, 0, 6)

    print("\nBranch and bound")
    print("Quantidade de nós analizados: " + str(number_graph_nodes_analyzed))
    print("Tamanho do caminho encontrado: " + str(length_found_path))
    print("Caminho entre o nó inicial e o nó final: " + str(path_between_start_and_goal))
    # endregion BRANCH AND BOUND

    reset_is_visited(graph)

    # region DFS
    number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal = dfs(graph, 0, 6)
    
    print("\nDFS")
    print("Quantidade de nós analizados: " + str(number_graph_nodes_analyzed))
    print("Tamanho do caminho encontrado: " + str(length_found_path))
    print("Caminho entre o nó inicial e o nó final: " + str(path_between_start_and_goal))
    # endregion DFS
    
    reset_is_visited(graph)

    # region BFS
    number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal = bfs(graph, 0, 6)
    
    print("\nBFS")
    print("Quantidade de nós analizados: " + str(number_graph_nodes_analyzed))
    print("Tamanho do caminho encontrado: " + str(length_found_path))
    print("Caminho entre o nó inicial e o nó final: " + str(path_between_start_and_goal))
    # endregion BFS
    
    # region A*
    number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal = a_star(graph, 0, 6)
    
    print("\nA*")
    print("Quantidade de nós analizados: " + str(number_graph_nodes_analyzed))
    print("Tamanho do caminho encontrado: " + str(length_found_path))
    print("Caminho entre o nó inicial e o nó final: " + str(path_between_start_and_goal))
    # endregion A*
