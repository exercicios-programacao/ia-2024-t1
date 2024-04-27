"""Implementação da busca em profundidade."""

def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    
    #Validando a existência dos nós
    try:
        graph[start]
        graph[goal]
    except IndexError:
        print("Node doesn't exist")
        return None

    stack = [ (start,None) ]
    visitedNodes = list()
    while ( len(stack) ):
        v = stack.pop()
        if goal == v[0]:
            predecessor = v[1]
            path = [ v[0], predecessor ]
            totalCost = v[2]
            countNodes = 1
            if predecessor != start:
                countNodes += 1
            while len(visitedNodes):
                temp = visitedNodes.pop()
                if predecessor == temp[0]:
                    predecessor = temp[1]
                    if predecessor != None:
                        totalCost += temp[2]
                        path.append(predecessor)
                        if predecessor != start:
                            countNodes += 1
            path.reverse()
            return (countNodes, totalCost, path)
        if not v in visitedNodes:
            visitedNodes.append(v)               
            for key, value in graph[v[0]][1].items():
                stack.append( (key, v[0], value) )


