from graph import get_neighbors

CONST_NEIGHBOR_VERTEX_INDEX = 0
CONST_WEIGHT_INDEX = 1
number_of_visited = 0
length = 0.0
path = []


def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando busca em profundidade."""
    stack = []
    visited = []
    stack.append((start, 0))  # starts with 0 because you are in the vertex

    while stack:
        edge = stack.pop()
        process(edge)
        if goal == edge[CONST_NEIGHBOR_VERTEX_INDEX]:
            return number_of_visited, length, path
        if edge not in visited:
            visited.append(edge[CONST_NEIGHBOR_VERTEX_INDEX])
            for new_edge in get_neighbors(graph, edge[CONST_NEIGHBOR_VERTEX_INDEX]):
                stack.append(new_edge)


def process(edge):
    global number_of_visited, length, path
    number_of_visited += 1
    path.append(edge[CONST_NEIGHBOR_VERTEX_INDEX])
    length += edge[CONST_WEIGHT_INDEX]
