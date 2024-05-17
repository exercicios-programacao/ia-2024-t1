"""Implementação do algoritmo de bfs."""

from util import mountpath


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    try:
        assert graph[start]
        assert graph[goal]
    except KeyError:
        print("Node doesn't exist")
        return None

    queue = [(start, None)]
    visited_nodes = {}
    count_nodes = 0

    while queue:
        curr_node, predecessor = queue.pop(0)

        if goal == curr_node:

            path, total_cost = mountpath(
                visited_nodes,
                curr_node,
                predecessor,
                graph
            )

            break

        if curr_node not in visited_nodes:
            count_nodes += 1
            visited_nodes[curr_node] = predecessor

            for neighbor, _ in graph[curr_node][1].items():
                if neighbor not in visited_nodes:
                    queue.append((neighbor, curr_node))

    return (count_nodes, total_cost, path)
