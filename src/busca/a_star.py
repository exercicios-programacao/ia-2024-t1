"""
Algoritmo de busca A*.

Algoritmo de busca A* para encontrar o menor caminho entre dois nós.
"""

# import json
from heapq import heappop, heappush

# Assuming util is imported from the project or a library
from util import haversine, makeDict2


def a_star(graph, start: int, goal: int) -> tuple:
    """
    Algoritmo de busca A* para encontrar o menor caminho entre dois nós.

    Args:
        graph (list): grafo com os nós e suas informações.
        start (int): nó inicial.
        goal (int): nó final.
    Returns:
        tuple: quantidade de nós visitados, custo do menor caminho e menor caminho.
    """

    grafo_dicionario = makeDict2(graph, goal)
    grafo_dicionario[start]["custo"] = 0
    visitados = set()
    heap = [(0, start)]

    while heap:  # enquanto heap não estiver vazio
        current_node = heappop(heap)[1]
        if current_node in visitados:
            continue
        visitados.add(current_node)
        if current_node == goal:
            break
        for visinho in grafo_dicionario[current_node]["visinhos"]:

            new_cost = (
                grafo_dicionario[current_node]["custo"]
                + grafo_dicionario[current_node]["visinhos"][visinho]
            )  # new_cost = cost_so_far[current] + graph.cost(current, next)
            if (
                new_cost < grafo_dicionario[visinho]["custo"]
                and visinho not in visitados
            ):  # if next not in cost_so_far or new_cost < cost_so_far[next]:
                print(visinho)
                grafo_dicionario[visinho][
                    "custo"
                ] = new_cost  # cost_so_far[next] = new_cost
                priority = new_cost + haversine(
                    grafo_dicionario[goal]["posicao"]["x"],
                    grafo_dicionario[goal]["posicao"]["y"],
                    grafo_dicionario[visinho]["posicao"]["x"],
                    grafo_dicionario[visinho]["posicao"]["y"],
                )  # priority = new_cost + heuristic(goal, next)
                heappush(heap, (priority, visinho))  # frontier.put(next, priority)
                grafo_dicionario[visinho][
                    "anteriores"
                ] = current_node  # came_from[next] = current
    # print(json.dumps(grafo_dicionario, indent=4))
    path = []
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = grafo_dicionario[current_node]["anteriores"]
    path.append(start)
    path.reverse()
    # para debug
    # with open("grafo.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(grafo_dicionario, indent=4))
    # return count, length, path
    return len(visitados), grafo_dicionario[goal]["custo"], path


# |   start0   |  goal7   |   count5   | [0, 2, 5, 7] |
