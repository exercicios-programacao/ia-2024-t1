def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""

    try:
        graph[start]
        graph[goal]
    except KeyError:
        print("Node doesn't exist")
        return None

    queue = [(start, None)]  
    visitedNodes = {} 
    count_nodes = 0

    while len(queue):
        currNode, predecessor = queue.pop(0)

        if goal == currNode:  
            path = [currNode]  
            totalCost = 0  
  
            while predecessor is not None: 
                path.append(predecessor)
                totalCost += graph[predecessor][1][currNode] 
                currNode = predecessor
                predecessor = visitedNodes.get(currNode) 

            path.reverse()  
            return (count_nodes, totalCost, path)

        if currNode not in visitedNodes:
            count_nodes += 1
            visitedNodes[currNode] = predecessor 
            
            for neighbor, cost in graph[currNode][1].items(): 
                if neighbor not in visitedNodes:  
                    queue.append((neighbor, currNode)) 
