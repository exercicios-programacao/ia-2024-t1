"""
Algoritmo de busca Dijkstra para encontrar o menor caminho entre dois nós.

funçoes:
    dijkstra: algoritmo de busca Dijkstra para encontrar o menor caminho entre dois nós.
    reconstruir_path: reconstrói o caminho a partir do nó final até o nó inicial.

"""

from heapq import heappop, heappush

from util import makeDict


def dijkstra(graph, start: int, goal: int):
    """
    Algoritmo de busca Dijkstra para encontrar o menor caminho entre dois nós.

    Args:
        graph (list): grafo com os nós e suas informações.
        start (int): nó inicial.
        goal (int): nó final.

    Returns:
        tuple: quantidade de nós visitados, custo do menor caminho e menor caminho.

    """
    grafo_dicionario = makeDict(graph)
    grafo_dicionario[start]["custo"] = 0
    visitados = set()
    heap = [(0, start)]

    while heap:  # enquanto heap não estiver vazio
        cost, current_node = heappop(heap)
        if current_node in visitados:
            continue
        visitados.add(current_node)

        if current_node == goal:
            shortest_path = reconstruir_path(grafo_dicionario, start, goal)
            return len(visitados), cost, shortest_path

        for visinho, distancia_visinho in grafo_dicionario[current_node][
            "visinhos"
        ].items():
            if visinho not in visitados:
                custo_total = cost + distancia_visinho
                if custo_total < grafo_dicionario[visinho]["custo"]:
                    grafo_dicionario[visinho]["custo"] = custo_total
                    grafo_dicionario[visinho]["anteriores"] = [current_node]
                    heappush(heap, (custo_total, visinho))
                elif custo_total == grafo_dicionario[visinho]["custo"]:
                    grafo_dicionario[visinho]["anteriores"].append(current_node)

    # não encontrou caminho
    return len(visitados), float("inf"), []


def reconstruir_path(graph, start, goal):
    """
    Reconstrói o caminho a partir do nó final até o nó inicial.

    Args:
        graph (dict): grafo com os nós e suas informações.
        start (int): nó inicial.
        goal (int): nó final.

    Returns:
        list: caminho do nó inicial até o nó final."""
    path = [goal]
    while path[-1] != start:
        current = path[-1]
        previouscurrent_nodes = graph[current]["anteriores"]
        if not previouscurrent_nodes:
            return []  # no path
        path.append(previouscurrent_nodes[0])
    return list(reversed(path))
