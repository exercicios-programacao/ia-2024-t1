"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""
from heapq import heappush, heappop


def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca o menor caminho entre start e goal usando o algoritmo dijkstra."""
    nodes_queue = []
    processed_nodes = []
    temp_nodes = {}
    heappush(nodes_queue, (0, start))

    temp_nodes[start] = {
        'predecessor': None,
        'curr_weight': 0,
        'all_predec': [None]
    }

    while nodes_queue:
        _, node = heappop(nodes_queue)

        if node in processed_nodes:
            continue

        processed_nodes.append(node)

        if node == goal:
            path = [goal]
            current_path = goal

            while path[-1] != start:
                current_path = temp_nodes[current_path]['predecessor']
                path.append(current_path)

            path.reverse()

            break

        visited_node = temp_nodes[node]
        for neighbor_node, neighbor_weight in graph[node][1].items():
            if (
                neighbor_node not in temp_nodes or
                node not in temp_nodes[neighbor_node]['all_predec']
            ):
                new_weight = visited_node['curr_weight'] + neighbor_weight
                new_predec = node

                if neighbor_node not in temp_nodes:
                    heappush(nodes_queue, (new_weight, neighbor_node))
                    temp_nodes[neighbor_node] = {
                        'predecessor': new_predec,
                        'curr_weight': new_weight,
                        'all_predec': [new_predec]
                    }
                elif new_weight < temp_nodes[neighbor_node]['curr_weight']:
                    heappush(nodes_queue, (new_weight, neighbor_node))
                    new_all_predec = temp_nodes[neighbor_node]['all_predec']
                    new_all_predec.append(new_predec)

                    temp_nodes[neighbor_node] = {
                        'predecessor': new_predec,
                        'curr_weight': new_weight,
                        'all_predec': new_all_predec
                    }
                else:
                    temp_nodes[neighbor_node]['all_predec'].append(new_predec)

    return (
        len(processed_nodes),
        temp_nodes[node]['curr_weight'],
        path
    )
