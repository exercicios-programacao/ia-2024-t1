from heapq import heappop, heappush

from util import makeDict


def dijkstra(graph, start: int, goal: int):
    graphDict = makeDict(graph)
    graphDict[start]["custo"] = 0
    visitados = set()
    heap = [(0, start)]

    while heap:  # enquanto heap não estiver vazio
        cost, currentNode = heappop(heap)
        if currentNode in visitados:
            continue
        visitados.add(currentNode)

        if currentNode == goal:
            shortestPath = reconstruirPath(graphDict, start, goal)
            return len(visitados), cost, shortestPath

        for visinho, distanciaVisinho in graphDict[currentNode]["visinhos"].items():
            if visinho not in visitados:
                custoTotal = cost + distanciaVisinho
                if custoTotal < graphDict[visinho]["custo"]:
                    graphDict[visinho]["custo"] = custoTotal
                    graphDict[visinho]["anteriores"] = [currentNode]
                    heappush(heap, (custoTotal, visinho))
                elif custoTotal == graphDict[visinho]["custo"]:
                    graphDict[visinho]["anteriores"].append(currentNode)

    # não encontrou caminho
    return len(visitados), float("inf"), []


def reconstruirPath(graph, start, goal):
    path = [goal]
    while path[-1] != start:
        current = path[-1]
        previouscurrentNodes = graph[current]["anteriores"]
        if not previouscurrentNodes:
            return []  # no path
        path.append(previouscurrentNodes[0])
    return list(reversed(path))
