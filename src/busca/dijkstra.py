from heapq import heappop, heappush

from util import makeDict


def dijkstra(graph, start: int, goal: int):
    graphDict = makeDict(graph)
    graphDict[start]["custo"] = 0
    visitados = set()
    heap = [(0, start)]

    while heap:  # enquanto heap não estiver vazio
        cost, node = heappop(heap)
        if node in visitados:
            continue
        visitados.add(node)

        if node == goal:
            shortestPath = reconstruirPath(graphDict, start, goal)
            return len(visitados), cost, shortestPath

        for visinho, distanciaVisinho in graphDict[node]["visinhos"].items():
            if visinho not in visitados:
                custoTotal = cost + distanciaVisinho
                if custoTotal < graphDict[visinho]["custo"]:
                    graphDict[visinho]["custo"] = custoTotal
                    graphDict[visinho]["anteriores"] = [node]
                    heappush(heap, (custoTotal, visinho))
                elif custoTotal == graphDict[visinho]["custo"]:
                    graphDict[visinho]["anteriores"].append(node)

    # não encontrou caminho
    return len(visitados), float("inf"), []


def reconstruirPath(graph, start, goal):
    path = [goal]
    while path[-1] != start:
        current = path[-1]
        previousNodes = graph[current]["anteriores"]
        if not previousNodes:
            return []  # no path
        path.append(previousNodes[0])
    return list(reversed(path))
