from heapq import heappop, heappush

# Assuming util is imported from the project or a library
from util import makeDict2


def a_star(graph, start: int, goal: int) -> tuple:
    graphDict = makeDict2(graph, goal)
    graphDict[start]["custo"] = 0
    visitados = set()
    heap = [(0, start)]

    while heap:  # enquanto heap não estiver vazio
        currentNode = heappop(heap)[1]
        if currentNode in visitados:
            continue
        visitados.add(currentNode)
        if currentNode == goal:
            break
        for visinho, cost in graph[currentNode][1]:
            if visinho not in visitados:
                newCost = graphDict[currentNode]["custo"] + cost
                if newCost < graphDict[visinho]["custo"]:
                    graphDict[visinho]["custo"] = newCost
                    priority = newCost + graphDict[visinho]["goalDistance"]
                    heappush(heap, (priority, visinho))
                    graphDict[visinho]["anteriores"] = currentNode
    # print(json.dumps(graphDict, indent=4))
    path = []
    currentNode = goal
    while currentNode != start:
        path.append(currentNode)
        currentNode = graphDict[currentNode]["anteriores"]
    path.append(start)
    path.reverse()
    # return count, length, path
    return len(visitados), graphDict[goal]["custo"], path


# |   start0   |  goal7   |   count5   | [0, 2, 5, 7] |
