"""Utilize este arquivo para depurar seus algoritmos."""

import os

from busca import a_star, bfs, branch_and_bound, dfs, dijkstra
from graph import read_graph

if __name__ == "__main__":
    grafo = read_graph("ia-2024-t1/mapas/mini_map.txt")
    # grafo = read_graph("ia-2024-t1/micro_mapas/_map.txt")
    # grafo = read_graph("ia-2024-t1/mapas/small_map.txt")
    # grafo = read_graph("ia-2024-t1/mapas/medium_map.txt")
    # grafo = read_graph("ia-2024-t1/mapas/full_map.txt")
    # caminho_dfs = dfs(grafo, 0, 9)
    # caminho_bfs = bfs(grafo, 0, 9)
    caminho_bb = branch_and_bound(grafo, 0, 9)
    # caminho_dijkstra = dijkstra(grafo, 0, 9)
    # os.system("cls")
    # print("148|", a_star(grafo, 0, 764))
    # print("-" * 10)
    # print("133|", a_star(grafo, 230, 850))

# | start | goal | count | path            |
# |   0   | 764  |  148  | [0, 709, 710, 712, 714, 716, 718, 722, 727, 730, 734, 738, 743, 744, 748, 751, 752, 755, 758, 762, 763, 764] |
# |   230 | 850  |  133  | [230, 229, 228, 227, 226, 225, 218, 217, 216, 215, 214, 213, 895, 887, 884, 883, 873, 872, 871, 870, 852, 851, 850] |

# print(caminho_dfs)
# print(caminho_bfs)
print(caminho_bb)
# print(caminho_dijkstra)
# print(caminho_a_star)
