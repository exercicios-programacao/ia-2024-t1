def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando branch and bound."""

    try:
        graph[start]
        graph[goal]
    except KeyError:
        print("Node doesn't exist")
        return None

    queue = [(start, None)]
    visitedNodes = {} 
    best_path = None
    best_cost = float('inf')
    count_nodes = 0;

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
            if totalCost < best_cost:
                best_path = path
                best_cost = totalCost
            continue

        if currNode not in visitedNodes:
            count_nodes += 1
            visitedNodes[currNode] = predecessor 

            for neighbor, cost in graph[currNode][1].items(): 
                if neighbor not in visitedNodes and cost < best_cost:
                    queue.append((neighbor, currNode))

    if best_path is not None:
        return (count_nodes, best_cost, best_path)