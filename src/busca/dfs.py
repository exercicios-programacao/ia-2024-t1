from graph import get_neighbors

CONST_NEIGHBOR_VERTEX_INDEX = 0
CONST_WEIGHT_INDEX = 1
length = 0.0
path = []


def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando busca em profundidade."""
    stack = []
    visited = []
    stack.append((start, 0))  # starts with 0 because you are in the vertex
    is_first = True
    while stack:
        edge = stack.pop()
        if goal == edge[CONST_NEIGHBOR_VERTEX_INDEX]:
            process(edge)
            return len(visited), length, path
        if edge[CONST_NEIGHBOR_VERTEX_INDEX] not in visited:
            process(edge)
            visited.append(edge[CONST_NEIGHBOR_VERTEX_INDEX])
            for new_edge in get_neighbors(graph, edge[CONST_NEIGHBOR_VERTEX_INDEX]):
                stack.append(new_edge)


def process(edge):
    global length, path
    path.append(edge[CONST_NEIGHBOR_VERTEX_INDEX])
    length += edge[CONST_WEIGHT_INDEX]
