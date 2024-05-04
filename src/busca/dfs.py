
"""Implementação da busca em profundidade."""

from typing import List
from util import *
from graph import Vertex


def dfs(graph: List[Vertex], start: int, goal: int) -> (int, float, [int]):
    if check_vertex_in_graph(graph, start) or check_vertex_in_graph(graph, goal):
        raise Exception("Os valores start e/ou goal não existem no grafo")

    number_graph_nodes_analyzed: int = 0
    stack: List[List[int]] = [[start]]

    while stack:
        if stack[-1][-1] == goal:
            path_between_start_and_goal = stack[-1]
            length_found_path = get_length_path(graph, path_between_start_and_goal)
            return number_graph_nodes_analyzed, length_found_path, path_between_start_and_goal
        else:
            node_list = stack.pop()
            number_graph_nodes_analyzed += 1
            adjacent_vertex_list: List[AdjacentVertex] = next(filter(lambda e: e.Vertex == node_list[-1], graph), None).AdjacentVertexList
            stack.extend(find_neighbor(graph, node_list, adjacent_vertex_list, goal))

    raise Exception(f"É impossível encontrar um caminho entre {start} e {goal}")


"""Busca um caminho entre start e goal usando busca em profundidade"""
