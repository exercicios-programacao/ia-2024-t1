import json
from heapq import heappop, heappush

# Assuming util is imported from the project or a library
from util import haversine, makeDict2


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
        for visinho in graphDict[currentNode]["visinhos"]:

            newCost = (
                graphDict[currentNode]["custo"]
                + graphDict[currentNode]["visinhos"][visinho]
            )  # new_cost = cost_so_far[current] + graph.cost(current, next)
            if (
                newCost < graphDict[visinho]["custo"] and visinho not in visitados
            ):  # if next not in cost_so_far or new_cost < cost_so_far[next]:
                print(visinho)
                graphDict[visinho]["custo"] = newCost  # cost_so_far[next] = new_cost
                priority = newCost + haversine(
                    graphDict[goal]["posicao"]["x"],
                    graphDict[goal]["posicao"]["y"],
                    graphDict[visinho]["posicao"]["x"],
                    graphDict[visinho]["posicao"]["y"],
                )  # priority = new_cost + heuristic(goal, next)
                heappush(heap, (priority, visinho))  # frontier.put(next, priority)
                graphDict[visinho][
                    "anteriores"
                ] = currentNode  # came_from[next] = current
    # print(json.dumps(graphDict, indent=4))
    path = []
    currentNode = goal
    while currentNode != start:
        path.append(currentNode)
        currentNode = graphDict[currentNode]["anteriores"]
    path.append(start)
    path.reverse()
    with open("grafo.json", "w") as f:
        f.write(json.dumps(graphDict, indent=4))
    # return count, length, path
    return len(visitados), graphDict[goal]["custo"], path


# |   start0   |  goal7   |   count5   | [0, 2, 5, 7] |
